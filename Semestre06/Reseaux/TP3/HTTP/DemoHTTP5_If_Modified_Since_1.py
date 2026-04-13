# -*- @author: Ilyas Bambrik -*-

#Last-Modified: Mon, 07 Jun 2004 00:26:52 GMT Code reponse 304
import socket
ConnexionAuServeurHTTP=socket.socket()
Serveur="www.tcpipguide.com"
Port=80
ConnexionAuServeurHTTP.connect((Serveur,Port))
# requete avec header If-Modified-Since (telecharger la ressource si celle-ci a ete modifi[&e] au dela de la data specifi[&e] par If-Modified-Since
ConnexionAuServeurHTTP.send(b"GET /free/diagrams/tcpswunack.png HTTP/1.1\r\nHost:www.tcpipguide.com\r\nIf-Modified-Since: Mon, 07 Jun 2005 00:26:52 GMT\r\nConnexion:close\r\n\r\n")

rec=ConnexionAuServeurHTTP.recv(1024)
while True:
    if len(rec)==0:
        break
    print(rec.decode("unicode_escape"),)
    rec=ConnexionAuServeurHTTP.recv(1024)
