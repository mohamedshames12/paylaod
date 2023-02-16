import socket
import os
# my server
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.1.2",4444))
    s.listen(5)
    client , addr = s.accept()
    print("Connecting from {0}:{1}".format(addr[0],addr[1]))
    while True:
        data = client.recv(500000)
        print(data.decode("utf-8"))
        command = str(input(" < command > "))
        client.send(command.encode("utf-8"))
except socket.error as e:
    print(e)