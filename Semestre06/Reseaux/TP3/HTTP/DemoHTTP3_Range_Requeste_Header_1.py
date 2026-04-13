# -*- @author: Ilyas Bambrik -*-

## Lire l'explication de DemoHTTP1_GET avant de lire ce document

# Range (demande de contenu partiel) / [ reponse serveur ContentRange - Code 206 contenu partiel]

import socket
ConnexionAuServeurHTTP=socket.socket()
Serveur="www.tcpipguide.com"
Port=80
ConnexionAuServeurHTTP.connect((Serveur,Port))
# L'entete [Range: bytes=500-1000] indique que le client souhaite recevoir seulemnt les octets de 500 jusqu'a 1000
# Demande des caracteres dans l'intervale 500-1000
ConnexionAuServeurHTTP.send(b"GET / HTTP/1.1\r\nHost:www.tcpipguide.com\r\nRange: bytes=500-1000\r\nConnexion:close\r\n\r\n")
rec=ConnexionAuServeurHTTP.recv(1024)
while True:
    if len(rec)==0:
        break
    print(rec.decode("unicode_escape"),)
    rec=ConnexionAuServeurHTTP.recv(1024)
