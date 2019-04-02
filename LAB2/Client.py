import socket
import select
import string
import sys

def view() :
	sys.stdout.flush()

def main():
    host = '128.171.8.114'
    port = 4063
    
    name=raw_input("\n Enter Your name: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((host, port))
    s.send(name)
    view()
    while 1:
        socket_list = [sys.stdin, s]
        rList, wList, error_list = select.select(socket_list , [], [])
        for sock in rList:
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print '\n DISCONNECTED'
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    view()
            else :
                msg=sys.stdin.readline()
                s.send(msg)
                view()

if __name__ == "__main__":
    main()