
# -*- coding: cp1252 -*-
# -*- @author: Ilyas Bambrik -*-
import socket
connexionTCP=socket.socket()
import ssl
Serveur="www.coursera.org" 
Port=443

connexionTCP.connect((Serveur,Port))
ConnexionAuServeurHTTPS=ssl.create_default_context().wrap_socket(connexionTCP,server_hostname=Serveur)

ConnexionAuServeurHTTPS.send(b"GET /api/certificate.v1/pdf/Z5YYKY5RSFHZ HTTP/1.1\r\nHost:www.coursera.org\r\nConnection:close\r\n\r\n")
rec=b""
while 1:
        if b"\r\n\r\n" in rec:
                break
        rec+=ConnexionAuServeurHTTPS.recv(1024)
rec=rec[rec.find(b"\r\n\r\n")+4::]
fichier_=open("fichier3.pdf","wb")
while True:
        if len(rec)==0:
                break
        fichier_.write(rec)
        rec=ConnexionAuServeurHTTPS.recv(1024)
fichier_.close()
ConnexionAuServeurHTTPS.close()
