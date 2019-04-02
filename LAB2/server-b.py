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
		while True:
				print('status: Waiting for the incoming connections.........')
				soc.listen(1)
				conn, addr = soc.accept()
				ip = conn.recv(1024)
				if ip != "":
					conn.send(data)
					print('status: Connection established with the '+ip)
					break

	else:
		print "Client :"+str(data)
	




