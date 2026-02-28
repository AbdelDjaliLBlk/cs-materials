import socket
SocketServeur=socket.socket()
SocketServeur.bind(("0.0.0.0",50000))
SocketServeur.listen(4)
while True:
	ConnexionAuClient, addr = SocketServeur.accept()
	print(addr)
	print(ConnexionAuClient.recv(1024))
	ContenuReponse="<html><body><h1>FAKEHTMLSERVER INC &#xa9;</h1></body></html>"
	ReponseServeur="HTTP/1.1 200 OK\r\nDate: Thu, 17 Jan 2019 13:18:42 GMT\r\nServer: Apache/2.4.37\r\nAccept-Ranges: bytes\r\nContent-Length: %d\r\nContent-Type:HTML\r\n\r\n"%(len(ContenuReponse))
	ConnexionAuClient.send(ReponseServeur.encode())
	ConnexionAuClient.send(ContenuReponse.encode())
	ConnexionAuClient.close()
