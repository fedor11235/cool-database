#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import json
import sys

def funcData(data):
    print("\nЧто пришло: ", data)
    data = json.loads(data)
    print("\nВыделили нужную инфу: ", data)

    mess = "Мы получили ваше сообщение!!!".encode('utf-8')

    return mess

host = ''
port = 2222

sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
while True: 
    conn, addr = sock.accept()

    print ('\nПодключился клиент: ', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        
        conn.send(funcData(data))

conn.close()