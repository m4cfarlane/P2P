import socket

def Server():
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind(('localhost', 8090))
	serversocket.listen(5) # become a server socket, maximum 5 connections

	while True:
	    connection, address = serversocket.accept()
	    buf = connection.recv(64)
	    bufdecode = buf.decode("utf-8")
	    if bufdecode == 'hello':
	        print("Received message '{}', replying...".format(bufdecode))
	        connection.send(bytes('hi', 'utf-8'))
	        break

Server()

'''
Use TCP SYN-ACK ACK for connections
'''
