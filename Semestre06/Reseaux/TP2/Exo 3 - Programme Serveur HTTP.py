import socket
SocketServeur=socket.socket()
SocketServeur.bind(("0.0.0.0",5000))
SocketServeur.listen(4)
while True:
	ConnexionAuClient, addr = SocketServeur.accept()
	print(ConnexionAuClient, addr)
	print(ConnexionAuClient.recv(1024))
	ConnexionAuClient.send(b"\r\n\r\n<html><body><h1>FAKEHTMLSERVER INC &#xa9;</h1></body></html>")
	ConnexionAuClient.close()
