# -*- coding: cp1252 -*-
# OPTIONS :

import socket
ConnexionAuServeurHTTP=socket.socket()
Serveur="www.tcpipguide.com"
Port=80
ConnexionAuServeurHTTP.connect((Serveur,Port))
ConnexionAuServeurHTTP.send(b"OPTIONS / HTTP/1.1\r\nHost:www.tcpipguide.com\r\nConnexion:close\r\n\r\n")

rec=ConnexionAuServeurHTTP.recv(1024)
while True:
    if len(rec)==0:
        break
    print(rec.decode("unicode_escape"),)
    rec=ConnexionAuServeurHTTP.recv(1024)
