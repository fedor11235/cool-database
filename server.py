#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import random
from moduls import ProtoHelper
from moduls import Conf
from moduls import Cheksum
import json

packetTypes = {
    "0x1": "auth_request", #запрос авторизации #нечётные клиента и чётные от сервера
    "0x8001": "auth_response", #ответ авторизации
    "0x2": "get_request", #запрос на чтение данных
    "0x2001": "get_response", #ответ на чтение данных
}

def BuildData(code, payloadClient, idSessions): 

    payload = b""
    data = b""

    if code == "0x1":

        autor = False

        with open("bd/users.json") as f:
            templates = json.load(f)

        users = templates["users"]
        for user in users:
            if user["login"] == payloadClient["login"]:
                if user["password"] == payloadClient["password"]:
                    autor = True
                    
        if autor:
            idSessions = random.random()
            payloadDict = {"idSessions": idSessions, "message": "All right auth"}

        else:
            payloadDict = {"idSessions": idSessions, "message": "You are not authorized"}

        payload = ProtoHelper.Encode("auth_response", payloadDict)

    if code == "0x2":
        
        if payloadClient["idSessions"] == str(idSessions):
            selection = {}
            selectionKey = ""

            with open("bd/data.json") as f:
                templates = json.load(f)


            keys = payloadClient["keys"]
            number = payloadClient["number"]

            keys = keys.split(" ")

            for i in range(int(number)):
                for key in keys:
                    for numbers in number:
                        selectionKey += str(templates[key])
                    selection.update({key: selection})    

            payloadDict = {"idSessions": idSessions, "message": selection}

        else: 
            payloadDict = {"idSessions": idSessions, "message": "You cannot send requests"}
        payload = ProtoHelper.Encode("get_response", payloadDict)

    if code == "0x0":

        payloadDict = {"idSessions": idSessions, "message": "Damaged package"}
        payload = ProtoHelper.Encode("get_response", payloadDict)
    
    cheksum=Cheksum.Cheksum(payload)
    data = 0x7f.to_bytes(1, "big") + payload + cheksum.to_bytes(2, "big") + 0x7f.to_bytes(1, "big")

    return data, idSessions

def ServerRecvLoop(conn, idSessions):

    isRecvPacketProgess = False
    packetData = b''

    while True:
        recvData = conn.recv(8) 
        
        identyPosL = recvData.find(b'\x7f')
        if isRecvPacketProgess :
            packetData += recvData

        if not isRecvPacketProgess and identyPosL >= 0:
            isRecvPacketProgess = True
            packetData += recvData[identyPosL:len(recvData)]      
        
        identyPosR = packetData.rfind(b'\x7f')
        if identyPosR > 0 and identyPosL != identyPosR:
            print("End of package")
            print(identyPosL, identyPosR)
            packetData=packetData[1:identyPosR] #identyPosL без -6 при запросе данных

            cheksum = Cheksum.CheksumTransportPackech(packetData)
            if not cheksum:

                print("Damaged package")
                data, idSessions = BuildData("0x0", 0, idSessions)
                return data

            else: 
                payloadBin = packetData[0:len(packetData)-2]
                packet = packetTypes[ProtoHelper.GetDecodeСode(payloadBin[0:2])]
                payloadClient = ProtoHelper.Decode(packet, payloadBin)

                data, idSessions = BuildData(payloadClient["code"], payloadClient, idSessions)  

                return data, idSessions

sock = socket.socket()
sock.bind((Conf.HOST, Conf.PORT))
sock.listen(5)
idSessions = None
while True: 
    
    conn, addr = sock.accept()
    print ("\nПодключился клиент: ", addr)
    data, idSessions = ServerRecvLoop(conn, idSessions)

    conn.send(data)

conn.close()
    