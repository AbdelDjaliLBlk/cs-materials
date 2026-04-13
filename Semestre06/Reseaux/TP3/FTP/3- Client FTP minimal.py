import socket
import re
ConnexionAUnServeur = socket.socket()

# Entrez l'adresse IP du serveur FTP depuis le clavier
print ("Entrez l'adresse IP du serveur FTP depuis le clavier :")
host = input() 
port = 21 # numero de port
ConnexionAUnServeur.connect((host, port)) # etablisement de connexion avec le

while True:
    recu=""
    while True:
              recu+=ConnexionAUnServeur.recv(2028).decode()
              m=re.findall("\d\d\d ",recu)
              if len(m)!=0:
                        break
    print(recu)
    commande=input().encode()
    ConnexionAUnServeur.send(commande+b"\r\n")
    
ConnexionAUnServeur.close() 


"""
 Il faut ajouter la commande PASV et l'extraction du IP et le port 20 (responsable de l'échange de données)
un autre socket pour se connecter au canal de données et enfin l'écriture dans un fichier et le sauvegarder
 """