#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import hashlib
import json
from moduls import ProtoHelper
from moduls import Conf
from moduls import Cheksum
import time

def Autor():
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
#idSessions = Autor()

#запрос на получение данных
RequestToReceive(idSessions)

sock.close()




