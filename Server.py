import socket				//importing the socket library
IP='192.41.233.53'			//Server Node IP Address
PORT_NUM=4366			//Port Number
soc=socket.socket()
print ('status: Waiting for the incoming connections.........')
soc.bind((IP,PORT_NUM))		//Binding with the client to listen
soc.listen(1)
conn,addr=soc.accept()
data = conn.recv(1000)		//receiving data from the client with particular size
if data == 'connected':
        print ('status: Connection established with the Client')
while True:
        data=conn.recv(1000)		//receiving data from the client with particular size
        if data=='Bye Server':
                conn.send('Bye Sampath (Message from the server)')
                print('Connection closed with client')
                break
        elif data=='Hello Server':
                print str(data)
                print ('........Message received from the client.......')
                conn.send('Hello Sampath (Message from the server)')
        else:
                print('.........Message received from the client......')
                print str(data)
                conn.send(data)
c.close()
