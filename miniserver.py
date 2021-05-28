#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import json
import sys
import ProtoHelper

def funcData(data):
    print("\nЧто пришло: ", data)
    data = json.loads(data)

    clientCheksum=data[0]+data[5]

    print("\nПришедшая контрольная сумма: ", clientCheksum)

    dataBytes = json.dumps(data).encode('utf-8')
    checksum = 0
    for ch in dataBytes:
        checksum += ch
    print("\nВычесленная контрольная сумма: ", checksum)

    if (clientCheksum!=checksum):
        print("\nКонтрольные суммы не совпадают")
        mess = "Ошибка в пакете".encode('utf-8')
        return(mess)

    print("\nВыделили нужную инфу: ", data[3])

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
        print ("\nПриняли от клиента:", list(data))

        #data2=ProtoHelper.Decode('auth_request', data)
        #print(data2, "На стороне сервера")

        if not data:
            break
        
        conn.send(ProtoHelper.Encode('auth_response', "All is ready"))

conn.close()