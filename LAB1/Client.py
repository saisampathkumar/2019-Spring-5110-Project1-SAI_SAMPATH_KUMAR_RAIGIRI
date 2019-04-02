import socket			//importing the socket library
IP='192.41.233.53' 		//Server Node IP Address
PORT_NUM=4366 		//Port Number
soc=socket.socket() 		
soc.connect((host,port))	//Connecting the server
soc.send('connected')		//sending connection response to the server
print ('status : Connected to the server')
mes=raw_input("enter -->")	//Taking input from the terminal

while True:
        if mes == 'Bye Server':
                print('..............Message from the client.............')
                soc.send(mes)		//sending data to the server
                data=soc.recv(1000)	//receiving data from the server with particular size
                print str(data)
                print('Connection Closed with server')
                break
                mes=raw_input()
        elif mes == 'Hello Server':
                print('...............Message from the client..........')
                soc.send(mes)		//sending data to the server
                data=soc.recv(1000)	//receiving data from the server with particular size
                print str(data)
                mes= raw_input()
        else:
                soc.send(mes)		//sending data to the server
                data=soc.recv(1000)	//receiving data from the server with particular size
                print('.............Message from the client........')
                print str(data)
                print ('...........Enter Some other data Sampath..........')
                mess= raw_input()
soc.close()
