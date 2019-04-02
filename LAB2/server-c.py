import socket, select 
def send (soc, mess):
	for socket in connected_list:
		if socket != server_socket and socket != soc :
			try :
				socket.send(mess)
			except :
				socket.close()
				connected_list.remove(socket) 
if __name__ == "__main__":
	name=""
	record={}
	connected_list = []
	buffer = 4096
	port = 4062
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(("128.171.8.114", port))
	server_socket.listen(5)
	connected_list.append(server_socket)
	print "Waiting for Client Connection......"
	while 1:
		rList,wList,error_sockets = select.select(connected_list,[],[])
		
		for soc in rList:
			if soc == server_socket:
				conn, addr = server_socket.accept()
				name=conn.recv(buffer)
				connected_list.append(conn)
				record[addr]=name
				print "Client (%s, %s) connected" % addr," [",record[addr],"]"
				conn.send("Connection Established with the server")
				send(conn, name+" joined the conversation")
			else:
				data1 = soc.recv(buffer)
				data=data1[:data1.index("\n")]
				i,p=soc.getpeername()
				if data == "Bye Server":
					msg= record[(i,p)]+" left the conversation"
					send(soc,msg)
					print "Client (%s, %s) is offline" % (i,p)," [",record[(i,p)],"]"
					del record[(i,p)]
					connected_list.remove(soc)
					soc.close()
					continue
				else:
					msg="\n"+record[(i,p)]+": "
					print msg+data
						
	server_socket.close()
