#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import socket

def funcData():
    var = {'var0' : 0,   'var2' : 'some string', 'var1' : ['listiteпэк','listitem2',5]}

    varBytes = json.dumps(var).encode('utf-8')
    length = len(varBytes)

    lengtOne = length // 256
    lengthTwo = length % 256

    if lengtOne > 256:
        print("Введенные данные превышают допустимый размер")
        exit()

    data = [3, lengtOne, lengthTwo, var]
    data = json.dumps(data).encode('utf-8')
    return (data)

host = 'localhost'
port = 2222

sock = socket.socket()
sock.connect((host, port))
sock.send(funcData())

data = sock.recv(1024)
sock.close()

print ("\nОтвет от сервера:", data)
print ("\nПреобразованный ответ:", data.decode('utf-8'))