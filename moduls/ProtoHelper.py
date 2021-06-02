#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

packetTypes = {
    "auth_request": 0x0001, #запрос авторизации #нечётные клиента и чётные от сервера
    "auth_response":0x8001, #ответ авторизации
    "get_request": 0x0002, #запрос на чтение данных
    "get_response": 0x2001, #ответ на чтение данных
}

def BuildProtoString(in_str, out_len):
    out_str = bytearray(out_len)
    in_str = bytearray(str(in_str), encoding = "utf-8")
    out_str[0:len(in_str)] = in_str
    return out_str

def BuildDecodeString(in_str, start_cut, end_cut):
    out_str = in_str[start_cut:end_cut].decode("utf-8")
    out_str = out_str.replace("\x00", "")
    return out_str

def GetDecodeСode(in_str):
    out_str = int.from_bytes(in_str[0:2],"big")
    out_str = hex(out_str)
    return out_str

def Decode(packetType, payloadBin):

    payload=''
    if packetType == "auth_request":
        
        code = GetDecodeСode(payloadBin)
        login = BuildDecodeString(payloadBin, 2, 32)
        password = BuildDecodeString(payloadBin, 32, 64)

        payload = {"code":code, "login": login, "password": password}

    if packetType == "auth_response":

        code = GetDecodeСode(payloadBin)
        idSessions = BuildDecodeString(payloadBin, 2, 32)
        response = BuildDecodeString(payloadBin, 32, 62)

        payload={"code":code, "idSessions": idSessions, "response": response}

    if packetType=="get_request":
        
        code = GetDecodeСode(payloadBin)
        idSessions = BuildDecodeString(payloadBin, 2, 32)
        number = BuildDecodeString(payloadBin, 32, 62)
        key = BuildDecodeString(payloadBin, 62, 92)

        payload={"code":code, "idSessions": idSessions, "number": number, "keys": key}

    if packetType=="get_response":

        code = GetDecodeСode(payloadBin)
        idSessions = BuildDecodeString(payloadBin, 2, 32)
        response = BuildDecodeString(payloadBin, 32, 62)

        payload={"code":code, "idSessions": idSessions, "response": response}

    return payload

def Encode(packetType, payload):
    payloadBin = b''
    if packetType == "auth_request":
        login = payload["login"]
        password = payload["password"]
        payloadBin = BuildProtoString(login, 30) + BuildProtoString(password, 32)
    
    if packetType == "auth_response":
        idSessions = payload["idSessions"]
        message = payload["message"]
        payloadBin = BuildProtoString(idSessions, 30) + BuildProtoString(message, 30)

    if packetType=="get_request":
        
        idSessions = payload["idSessions"]
        number = payload["number"]
        keys = payload["keys"]
        payloadBin = BuildProtoString(idSessions, 30) + BuildProtoString(number, 30) + BuildProtoString(keys, 30)

    if packetType=="get_response":
        idSessions = payload["idSessions"]
        message = payload["message"]
        payloadBin = BuildProtoString(idSessions, 30) + BuildProtoString(message, 30)


    return packetTypes[packetType].to_bytes(2, "big") + payloadBin
    
