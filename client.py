#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import hashlib
from moduls import ProtoHelper
from moduls import Conf
from moduls import Cheksum

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

#авторизация
# password = hashlib.md5(b"pass11235").hexdigest() 
# authPayloadDict = {"login":"Fedor", "password": password} 
# data = BuildData("auth_request", authPayloadDict)

#запрос на получение данных
getPayloadDict = {"number": 1, "keys": "id"}
data = BuildData("get_request", getPayloadDict)


print(data)
sock.send(data)

payloadServer = ClientRecvLoop(sock)
sock.close()

print ("\nОтвет от сервера:", payloadServer)



