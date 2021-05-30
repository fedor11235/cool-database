#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from moduls import ProtoHelper
from moduls import Conf
from moduls import Cheksum
import json

def BuildData(code, payloadClient): 

    if code == "0x1":

        autor = False

        with open("users.json") as f:
            templates = json.load(f)

        users = templates["users"]
        for user in users:
            if user["login"] == payloadClient["login"]:
                if user["password"] == payloadClient["password"]:
                    autor = True
                    
        if autor:
            payload = ProtoHelper.Encode("auth_response", "All right auth")

        else:
            payload = ProtoHelper.Encode("auth_response", "You are not authorized")


    if code == "0x2":
        payload = ProtoHelper.Encode("get_response", "All right get")

    if code == "0x0":
        payload = ProtoHelper.Encode("get_response", "Damaged package")
    
    cheksum=Cheksum.Cheksum(payload)
    data = 0x7f.to_bytes(1, "big") + payload + cheksum.to_bytes(2, "big") + 0x7f.to_bytes(1, "big")

    return data

def ServerRecvLoop(conn):

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
            print(identyPosL)
            packetData=packetData[identyPosL-1:identyPosR]
            print(list(packetData))

            cheksum = Cheksum.CheksumTransportPackech(packetData)
            if not cheksum:
                print("Damaged package")
                data = BuildData("0x0", 0)
                return data

            else: 
                payloadBin = packetData[identyPosL-2:identyPosR-2]
                payloadClient=ProtoHelper.Decode('auth_request', payloadBin)
                data = BuildData(payloadClient["code"], payloadClient)
                return data

sock = socket.socket()
sock.bind((Conf.HOST, Conf.PORT))
sock.listen(5)

while True: 
    conn, addr = sock.accept()
    print ("\nПодключился клиент: ", addr)
    data = ServerRecvLoop(conn)
    conn.send(data)

conn.close()
    