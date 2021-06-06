import socket
import threading
import json
import sys

def read_sok():#фуyкция которая получает сообщения от сервера
    while 1 :
        data = sor.recv(1024)
        print(data.decode('utf-8'))
server = '192.168.0.1', 2222  #Данные сервера
alias = input() #Вводим наш псевдоним

sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0)) #Задаем сокет как клиент
sor.sendto((alias+' Connect to server').encode('utf-8'), server)   #Уведомляем сервер о подключении

potok = threading.Thread(target= read_sok)   #создаём поток и запускаем в нём функцию
potok.start()


while 1 :
    mensahe = input()
    sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)
sor.close()