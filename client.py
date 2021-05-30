#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import hashlib
from moduls import ProtoHelper
from moduls import Conf
from moduls import Cheksum

def BuildData(request, payloadDict): 
    
    payload = ProtoHelper.Encode(request, payloadDict)
    print(list(payload))
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
            packetData=packetData[identyPosL-1:identyPosR]

            cheksum = Cheksum.CheksumTransportPackech(packetData)
            if not cheksum:
                print("Damaged package")
                return "Damaged package"

            else: 
                payloadBin = packetData[identyPosL-2:identyPosR-3]
                data = ProtoHelper.Decode('auth_response', payloadBin)

                return data

sock = socket.socket()
sock.connect((Conf.HOST, Conf.PORT))

password = hashlib.md5(b"vargi").hexdigest() #1eabaea88304c48157e53c2a6f2a6ee9
authPayloadDict = {"login":"Danil", "password":"vargi"}

data = BuildData("auth_request", authPayloadDict)
sock.send(data)

payloadServer = ClientRecvLoop(sock)
sock.close()

print ("\nОтвет от сервера:", payloadServer)



