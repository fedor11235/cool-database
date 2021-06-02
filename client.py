#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import hashlib
import json
from moduls import ProtoHelper
from moduls import Conf
from moduls import Cheksum
import time

packetTypes = {
    "auth_request": 0x0001, #запрос авторизации #нечётные клиента и чётные от сервера
    "auth_response":0x8001, #ответ авторизации, удаление, изменение, регистрацию, удаление пользователя

    "get_request": 0x0002, #запрос на чтение данных
    "get_response": 0x2001, #ответ на чтение данных

    "delete_request": 0x0003, #запрос на удаление данных
    "change_request": 0x0004, #запрос на изменение данных
    "registration_request": 0x0005, #запрос на регистрацию пользователей
    "delete_users": 0x0006, #запрос на удаление пользователя
}

def RequestToAutor():
    password = hashlib.md5(b"pass11235").hexdigest() 
    authPayloadDict = {"login":"Fedor", "password": password} 
    dataAuth = BuildData("auth_request", authPayloadDict)

    sock.send(dataAuth)

    payloadServer = ClientRecvLoop(sock)
    print ("\nОтвет от сервера:", payloadServer)

    with open("bd/settings.json") as f:
        settings = json.load(f)
        settings["idSessions"] = payloadServer["idSessions"]

    with open('bd/settings.json', 'w') as f:
        json.dump(settings, f)

    return idSessions

def RequestToReceive(idSessions = None):

    getPayloadDict = {"idSessions":idSessions,"number": "1", "keys": "id"}
    dataGet = BuildData("get_request", getPayloadDict)
    sock.send(dataGet)
    payloadServer = ClientRecvLoop(sock)

    print ("\nОтвет от сервера:", payloadServer)

def RequestToDeleteData(idSessions = None):
    getPayloadDict = {"idSessions":idSessions,"keys": "created_at"}
    dataGet = BuildData("delete_request", getPayloadDict)
    sock.send(dataGet)
    payloadServer = ClientRecvLoop(sock)

    print ("\nОтвет от сервера:", payloadServer)

def RequestToChangeData(idSessions = None):
    getPayloadDict = {"idSessions":idSessions,"keys": "id full_text", "value":"3333 9999"}
    dataGet = BuildData("change_request", getPayloadDict)
    sock.send(dataGet)
    payloadServer = ClientRecvLoop(sock)

    print ("\nОтвет от сервера:", payloadServer)

def RequestToRegistration(idSessions = None):
    password = hashlib.md5(b"pass11235").hexdigest() 
    getPayloadDict = {"idSessions":idSessions,"login": "Rudi", "password":password}
    dataGet = BuildData("registration_request", getPayloadDict)
    sock.send(dataGet)
    payloadServer = ClientRecvLoop(sock)

    print ("\nОтвет от сервера:", payloadServer)

def RequestToDeleteUser(idSessions = None):
    password = hashlib.md5(b"pass11235").hexdigest() 
    getPayloadDict = {"idSessions":idSessions,"login": "Fedor", "password":password}
    dataGet = BuildData("delete_users", getPayloadDict)
    sock.send(dataGet)
    payloadServer = ClientRecvLoop(sock)

    print ("\nОтвет от сервера:", payloadServer)

def BuildData(request, payloadDict): 
    
    payload = ProtoHelper.Encode(request, payloadDict)
    cheksum = Cheksum.Cheksum(payload)
    data = 0x7f.to_bytes(1, "big") + payload + cheksum.to_bytes(2, "big") + 0x7f.to_bytes(1, "big")
    return data

def ClientRecvLoop(sock):

    isRecvPacketProgess = False
    packetData = b''
    while True:

        recvData = sock.recv(8)
        
        identyPosL = recvData.find(b'\x7f')
        if isRecvPacketProgess :
            packetData += recvData

        if not isRecvPacketProgess and identyPosL >= 0:
            isRecvPacketProgess = True
            packetData += recvData[identyPosL:len(recvData)]
        
        identyPosR = packetData.rfind(b'\x7f')
        if identyPosR > 0 and identyPosL != identyPosR:
            print("End of package")

            packetData=packetData[identyPosL:identyPosR]
            

            cheksum = Cheksum.CheksumTransportPackech(packetData)
            if not cheksum:
                return "Damaged package Client"

            else: 
                payloadBin = packetData[0:len(packetData)-2]
                data = ProtoHelper.Decode('auth_response', payloadBin)

                return data

sock = socket.socket()
sock.connect((Conf.HOST, Conf.PORT))

with open("bd/settings.json") as f:
    settings = json.load(f)
    idSessions = settings["idSessions"]

#авторизация
#idSessions = RequestToAutor()
#запрос на получение данных
#RequestToReceive(idSessions)
#запрос на изменение данных
#RequestToChangeData(idSessions)
#запрос на удаление данных
#RequestToDeleteData() #!!!!!!
#запрос на удаление пользователя
#RequestToDeleteUser(idSessions)
#регистрация
#RequestToRegistration()

sock.close()




