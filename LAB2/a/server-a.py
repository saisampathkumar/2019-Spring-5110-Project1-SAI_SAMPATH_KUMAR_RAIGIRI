# SERVER-a

import sys
import socket 

IP='128.171.8.114'
PORT_NUM=5003
soc=socket.socket()
print('status: Waiting for the incoming connections.........')
soc.bind((IP, PORT_NUM)) 
soc.listen(1) 
conn, addr = soc.accept()
ip=conn.recv(512)
print('status: Connection Established with '+ip);
while True:
	data=conn.recv(512)
	if data=='':
		print('Connection closed with the '+ip)
		break
	else:
		print "Client 1: "+str(data)
	


