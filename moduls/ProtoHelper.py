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

def BuildDecodeСode(in_str):
    out_str = int.from_bytes(in_str[0:2],"big")
    out_str = hex(out_str)
    return out_str

def Decode(packetType, payloadBin):

    payload=''
    if packetType == "auth_request":
    
        code = BuildDecodeСode(payloadBin)
        login = BuildDecodeString(payloadBin, 2, 30)
        password = BuildDecodeString(payloadBin, 32, 60)

        payload = {"code":code, "login": login, "password": password}

    if packetType == "auth_response":

        code = BuildDecodeСode(payloadBin)
        rand = BuildDecodeString(payloadBin, 2, 30)
        response = BuildDecodeString(payloadBin, 32, 60)

        payload={"code":code, "rand": rand, "response": response}

    if packetType=="get_request":
        
        code = BuildDecodeСode(payloadBin)
        number = BuildDecodeString(payloadBin, 2, 30)
        key = BuildDecodeString(payloadBin, 32, 60)

        payload={"code":code, "number": number, "key": key}

    if packetType=="get_response":

        code = BuildDecodeСode(payloadBin)
        rand = BuildDecodeString(payloadBin, 2, 30)
        response = BuildDecodeString(payloadBin, 32, 60)

        payload={"code":code, "rand": rand, "response": response}

    return payload

def Encode(packetType, payload):
    payloadBin = b''
    if packetType == "auth_request":
        login = payload["login"]
        password = payload["password"]
        payloadBin = BuildProtoString(login, 30) + BuildProtoString(password, 31)
    
    if packetType == "auth_response":
        rand=random.random()
        payloadBin = BuildProtoString(rand, 30) + BuildProtoString(payload, 31)

    if packetType=="get_request":
        # number = bytearray (payload[0], encoding = "utf-8")
        # key = bytearray (payload[1], encoding = "utf-8")
        # var = b"\x0002" + number + key
        number = payload["number"]
        key = payload["key"]
        payloadBin = BuildProtoString(number, 30) + BuildProtoString(key, 31)

    if packetType=="get_response":
        rand=random.random()
        # var = bytearray (str(rand), encoding = "utf-8")+bytearray (payload, encoding = "utf-8")
        payloadBin = BuildProtoString(rand, 30) + BuildProtoString(payload, 31)


    return packetTypes[packetType].to_bytes(2, "big") + payloadBin
    
