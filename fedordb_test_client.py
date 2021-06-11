#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import hashlib
from modules import ProtoHelper
from storage import Conf
from modules import Cheksum

from modules import Base



from modules import Transport
from modules import Session

packetTypes = {
    "auth_request": 0x0001, #запрос авторизации #нечётные клиента и чётные от сервера
    "auth_response":0x8001, #ответ авторизации, удаление, изменение, регистрацию, удаление пользователя

    "get_request": 0x0002, #запрос на чтение данных
    "get_response": 0x2001, #ответ на чтение данных

    "delete_request": 0x0003, #запрос на удаление данных
    "change_request": 0x0004, #запрос на изменение данных
    "registration_request": 0x0005, #запрос на регистрацию пользователей
    "delete_users": 0x0006, #запрос на удаление пользователя
}

def request_to_auth():
    password = hashlib.md5(b"pass11235").hexdigest() 
    authPayloadDict = {"login":"Fedor", "password": password} 
    dataAuth = build_data("auth_request", authPayloadDict)

    sock.send(dataAuth)

    payloadServer = client_recv_loop(sock)
    print ("\nОтвет от сервера:", payloadServer)

    bd = Base.load("bd/settingsCL.json", False)
    bd.set("idSessions",payloadServer["idSessions"])
    bd.dump()

    return idSessions

def request_to_receive(idSessions = None):
    getPayloadDict = {"idSessions":idSessions, "keys": "id"}
    dataGet = build_data("get_request", getPayloadDict)
    sock.send(dataGet)
    payloadServer = client_recv_loop(sock)

    print ("\nОтвет от сервера:", payloadServer)

def request_to_deleteData(idSessions = None):
    getPayloadDict = {"idSessions":idSessions,"keys": "id"}
    dataGet = build_data("delete_request", getPayloadDict)
    sock.send(dataGet)
    payloadServer = client_recv_loop(sock)

    print ("\nОтвет от сервера:", payloadServer)

def request_to_changeData(idSessions = None):
    getPayloadDict = {"idSessions":idSessions,"keys": "idu full_text", "value":"pop ioi"}
    dataGet = build_data("change_request", getPayloadDict)
    sock.send(dataGet)
    payloadServer = client_recv_loop(sock)

    print ("\nОтвет от сервера:", payloadServer)

def request_to_registration(idSessions = None):
    password = hashlib.md5(b"pass11235").hexdigest() 
    getPayloadDict = {"idSessions":idSessions,"login": "Rudi", "password":password}
    dataGet = build_data("registration_request", getPayloadDict)
    sock.send(dataGet)
    payloadServer = client_recv_loop(sock)

    print ("\nОтвет от сервера:", payloadServer)

def request_to_deleteUser(idSessions = None):
    password = hashlib.md5(b"pass11235").hexdigest() 
    getPayloadDict = {"idSessions":idSessions,"login": "Fedor", "password":password}
    dataGet = build_data("delete_users", getPayloadDict)
    sock.send(dataGet)
    payloadServer = client_recv_loop(sock)

    print ("\nОтвет от сервера:", payloadServer)



def client_recv_loop(sock):
    transport = Transport.TransportController(sock=sock)
    session = Session.ClientSession(transport=transport)
    session.do_login()
    while True:
        dataRx = sock.recv(1024)
        transport.on_recv(dataRx)

 

sock = socket.socket()
sock.connect((Conf.HOST, Conf.PORT))

bd = Base.load("bd/settingsCL.json", False)
idSessions = bd["idSessions"]

client_recv_loop(sock)

#авторизация
#idSessions = request_to_auth()

#запрос на получение данных
#RequestToReceive(idSessions)

#запрос на изменение данных
#RequestToChangeData(idSessions)

#запрос на удаление данных
#RequestToDeleteData(idSessions) 
#запрос на удаление пользователя
#RequestToDeleteUser(idSessions)
#регистрация
#RequestToRegistration(idSessions)

sock.close()




