#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import socket
from moduls import CRC16 
from moduls import ProtoHelper
from moduls import Conf

host = Conf.HOST
port = Conf.PORT

sock = socket.socket()
sock.connect((Conf.HOST, Conf.PORT))

authPayloadDict = {'login':'Fefe333ershe', 'password':'44'}
data = ProtoHelper.Encode("auth_request", authPayloadDict)
print ("\nЗапрос к серверу:", list(data))
sock.send(data)

data = sock.recv(1024)
sock.close()

print ("\nОтвет от сервера:", list(data))
print ("\nПреобразованный ответ:", data.decode("utf-8"))



