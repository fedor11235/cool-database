import socket

host = ''
port = 2222
backlog = 5 
size = 1024 
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind((host,port)) 
#s.listen(backlog) 
while True: 
    #client, address = s.accept() 
    #data = client.recv(size) 
    data , addres = s.recvfrom(1024)  #данные и адреса сокета
    print("!!!!!!!!!!!!", str(data))
    if data: 
        s.send(data) 

    if data == "close":
        s.send(data)
        s.close()
        break

    # if data: 
    #     client.send(data) 

    # if data == "close":
    #     client.send(data)
    #     client.close()
    #     break

    client.close()