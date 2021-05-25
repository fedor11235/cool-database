import socket
HOST = ''
PORT = 2222
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(u"{'username':'username', 'password':'password'}".encode('utf8'))