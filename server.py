#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import json
import sys
from moduls import ProtoHelper
from moduls import Conf

sock = socket.socket()
sock.bind((Conf.HOST, Conf.PORT))
sock.listen(1)
while True: 
    conn, addr = sock.accept()

    print ("\nПодключился клиент: ", addr)

    while True:
        data = conn.recv(1024)
        print ("\nПриняли от клиента:", list(data))

        data2=ProtoHelper.Decode('auth_request', data)
        print(data2, "На стороне сервера")

        if not data:
            break
        
        conn.send(ProtoHelper.Encode("auth_response", "All is ready"))

conn.close()