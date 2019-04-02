import socket				//importing the socket library
s = socket.socket()
IP = '192.41.233.53'			//Server Node IP Address
port= 5559				//Port Number
s.connect((IP,port))			//Connecting the server
print("connection established with the server....")
print("Transfering the file to client")
filename = str('Trasnfer.txt')		
file = open(filename,'rb')		//opening the file containing data
file_data = file.read(10000)		 
s.send(file_data)			//sending the data
filename = str('Trasnfer.txt')		
file = open(filename,'rb')
data = s.recv(10000)			//receiving the acknowledgement from the server
file.write(data)
print(data)
print("Data has been transmitted successfully")
