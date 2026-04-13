import socket
import ssl
import time
def RecevoirLaReponseServeur(ConnexionSecurise, Tag_Commande):
    Reponse_recu=ConnexionSecurise.recv(1024).decode("unicode_escape")
    Delimiteur_De_Fin_De_Reponse=Tag_Commande+" "
    while True:
        # lire la reponse jusqu'a atteindre la sequence de caratere Delimiteur_De_Fin_De_Reponse (TAG de la commande)
        if(Delimiteur_De_Fin_De_Reponse in Reponse_recu):
            break 
        Reponse_recu+=ConnexionSecurise.recv(1024).decode("unicode_escape")
    return Reponse_recu

NomDomaineDuServeurIMAP="imap.gmail.com"
ConnexionAuServeur=socket.socket()
ConnexionAuServeur.connect((NomDomaineDuServeurIMAP,993))
# creation d'une connexion securise
ConnexionSecurise=ssl.create_default_context().wrap_socket(ConnexionAuServeur,server_hostname=NomDomaineDuServeurIMAP)
Commande=""
# recevoir le message de connexion
print( ConnexionSecurise.recv(2048).decode("unicode_escape"))
TAG_Commande=""
while True:
    # lire la commande
    Commande=input()
    # cree un tag apartir de l'horloge systeme (time.time())
    TAG_Commande_Horloge=str(int(time.time()))
    # envoie de la commande avec le TAG horloge
    ConnexionSecurise.send((TAG_Commande_Horloge+" "+Commande+"\r\n").encode())
    print( RecevoirLaReponseServeur(ConnexionSecurise,TAG_Commande_Horloge))
    # si la commande tapee par le client == LOGOUT, sortir de la boucle de lecture de commandes
    if(Commande.strip().lower().startswith("logout")):
        break
ConnexionSecurise.close()
