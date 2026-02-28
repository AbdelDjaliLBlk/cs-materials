from socket import socket;from random import random;import time
List_mots=open("dictionnaire.txt").read().split("\n")
socket_serveur=socket()
socket_serveur.bind(("localhost",700))
socket_serveur.listen(10)
while True:
	connexion,_=socket_serveur.accept()
	start=time.time()
	mot_aleatoire=List_mots[int(random()*len(List_mots))]
	connexion.send((mot_aleatoire+"#ENDOFWORD").encode("ascii"))
	client_typed=connexion.recv(1024).decode("ascii")
	while "#END" not in client_typed:
		client_typed+=connexion.recv(1024).decode("ascii")
	if client_typed.split("#")[0]==mot_aleatoire:
		connexion.send(("Time to type ="+str(time.time()-start)+"#ENDOFGAME").encode("ascii"))
	else:
		connexion.send(b"#TYPINGERROR")
connexion.close()
