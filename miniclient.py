#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import socket
import CRC16 
import ProtoHelper

def funcData():
    var = {'var0' : 0,   'var2' : 'some string', 'var1' : ['listiteпэк','listitem2',5]}
    
    varBytes = json.dumps(var).encode('utf-8')
    checksum=CRC16.Crc16(varBytes)

    length = len(varBytes)

    lengtOne = length // 256
    lengthTwo = length % 256

    

    if lengtOne > 256:
        print("Введенные данные превышают допустимый размер")
        exit()

    authPayloadDict = {'login':'Fefe333ershe', 'password':'44'}
    # data = [3, lengtOne, lengthTwo, var]
    data = ProtoHelper.Encode('auth_request', authPayloadDict)


    #data = json.dumps(data).encode('utf-8')

    # checksum = 0
    # for ch in data:
    #     checksum += ch
    print("контрольная сумма: ", checksum)

    #data = [checksum/2, 3, lengtOne, lengthTwo, var, checksum/2]
    #data = json.dumps(data).encode('utf-8')

    return (data)

host = 'localhost'
port = 2222

sock = socket.socket()
sock.connect((host, port))
data=funcData()
print ("\nЗапрос к серверу:", list(data))
sock.send(data)

data = sock.recv(1024)
sock.close()





print ("\nОтвет от сервера:", list(data))
print ("\nПреобразованный ответ:", data.decode('utf-8'))



