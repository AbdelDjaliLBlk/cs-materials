# -*- coding: cp1252 -*-
# -*- @author: Ilyas Bambrik -*-

import socket
ConnexionAuServeurHTTP=socket.socket()

# nom de domaine du serveur web
Serveur="www.tcpipguide.com"
# numero de port 
Port=80

# connecte au serveur distant
ConnexionAuServeurHTTP.connect((Serveur,Port))
# transmet la requete GET. Les headers de la requetes se terminent pas CRLF (\r\n)
# la requete se termine par CRLFCRLF (\r\n\r\n)
ConnexionAuServeurHTTP.send(b"GET / HTTP/1.1\r\nHost:www.tcpipguide.com\r\nConnexion:close\r\n\r\n")

# Les deux entetes HTTP dans cette requete sont :
# 1) [Host:www.tcpipguide.com] (nomdu domaine du serveur web)
# 2) [Connexion:close] (pour cloturer la connection apres l'envoie de la reponse)

# recevoir le contenu de la page ( lire le contenu reçu du buffer en morceaux [chaine de caractere] de taille maximale <= 1024 )

rec=ConnexionAuServeurHTTP.recv(1024)
while True:
    # apres la cloture de la connexion, le nombre d'octets lu sera d'une taille de 0
    if len(rec)==0:
        break
    # imprime le contenu du morceau reçu
    
    print(rec.decode("unicode_escape"),)
    # lire un nouveau morceau
    rec=ConnexionAuServeurHTTP.recv(1024)
