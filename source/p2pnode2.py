import socket

def Client():
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect(('localhost', 8090))
	clientsocket.send(bytes('hello', 'UTF-8'))
	buf = clientsocket.recv(64)
	bufdecode = buf.decode("utf-8")
	if bufdecode == 'hi':
		print("Received message '{}' terminating connection...".format(bufdecode))
		clientsocket.close()
	else:
		print("An error has occured")

Client()