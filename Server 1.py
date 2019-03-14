import socket				//importing the socket library
s = socket.socket()			
IP = '192.41.233.53'			//Server Node IP Address
port = 5559				//Port Number
s.bind((IP,port))			//Binding with the client to listen
s.listen(1)
print("waiting for any incoming connections......")
conn, addr = s.accept()
print("Connection established with the client")
print('waiting for the file from the client')
filename = 'recieved.txt'		//Creating a file with name received.txt
file = open(filename,'wb')		//opening the file
file_data = conn.recv(10000)		// receiving the file data from the client
file.write(file_data)			// writing the data on to the newly created file
print (str(file_data))			//printing the file data
conn.send('received the data (Message from the server)')
file.close()
print("File has been received successfully")
