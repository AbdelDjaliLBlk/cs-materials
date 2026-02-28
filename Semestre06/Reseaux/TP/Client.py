import socket

ConnexionAUnServeur = socket.socket() # Creation de socket
host = "127.0.0.1" # adresse de la machine distante
port = 9500 # numero de port
print( "Console Client")
ConnexionAUnServeur.connect((host, port)) # connexion avec le serveur ( envoie flag SYN)
Message_A_Transmettre=""
while Message_A_Transmettre.lower()!="fin":
    Message_A_Transmettre=input() # lecture depuis le clavier
    ConnexionAUnServeur.send(Message_A_Transmettre.encode()) # transmettre le message vers le serveur
    # .encode() transforme une chaine de caracteres en bytes (suite d'octets)
ConnexionAUnServeur.close() # cloture de la connexion avec le serveur (envoie flag FIN) 
print( "Fin du programme")
