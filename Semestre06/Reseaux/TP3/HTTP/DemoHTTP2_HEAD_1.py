# -*- @author: Ilyas Bambrik -*-

## Lire l'explication de DemoHTTP1_GET avant de lire ce document

# requete HEAD (obtention des informations sur le contenu d'une ressource) 

import socket
ConnexionAuServeurHTTP=socket.socket()
Serveur="www.tcpipguide.com"
Port=80
ConnexionAuServeurHTTP.connect((Serveur,Port))

# l'url de cette requete = / (racine)
ConnexionAuServeurHTTP.send(b"HEAD / HTTP/1.1\r\nHost:www.tcpipguide.com\r\nConnexion:close\r\n\r\n")
rec=ConnexionAuServeurHTTP.recv(1024)
# lire le contenu jusqu'a la fin
while True:
    if len(rec)==0:
        break
    print(rec.decode("unicode_escape"),)
    rec=ConnexionAuServeurHTTP.recv(1024)
