import socket
import ssl

def RecevoirLaReponseServeur(ConnexionSecurise, Delimiteur_De_Fin_De_Reponse):
    Reponse_recu= ConnexionSecurise.recv(1024).decode("unicode_escape")
    if (("+OK" in Reponse_recu))and Delimiteur_De_Fin_De_Reponse=="":
        return Reponse_recu
    if ("-ERR" in Reponse_recu):
        return Reponse_recu
    while True:
        # lire la reponse jusqu'a atteindre la sequence de caratere Delimiteur_De_Fin_De_Reponse
        if(Delimiteur_De_Fin_De_Reponse in Reponse_recu):
            break 
        Reponse_recu+=ConnexionSecurise.recv(1024).decode("unicode_escape")
    return Reponse_recu

    
NomDomaineDuServeurPOP="pop.gmail.com"
ConnexionAuServeur=socket.socket()
ConnexionAuServeur.connect((NomDomaineDuServeurPOP,995))
# creation d'une connexion securise
ConnexionSecurise=ssl.create_default_context().wrap_socket(ConnexionAuServeur,server_hostname=NomDomaineDuServeurPOP)
Commande=""
# liste de commande pour les quels la reponse setermine par "\r\n.\r\n" (un point au debut de la ligne)
ListeCommande=["list","top","retr","uidl"]
while True:
    Delimiteur=""
    for command_terminer_par_unpoint in ListeCommande:
        # si la commande issue par le client appartient a ListeCommande
        # la reponse de cette commande doit se terminee par "\r\n.\r\n"
        if(Commande.strip().lower().startswith(command_terminer_par_unpoint)):
            Delimiteur="\r\n.\r\n"
        # les autres commande comme QUIT, PASS et  USER auront une seule ligne de reponse seulement(+OK ou -ERR )
    print(RecevoirLaReponseServeur(ConnexionSecurise,Delimiteur))
    if(Commande.strip().lower().startswith("quit")):
        break
    Commande=input()
    ConnexionSecurise.send((Commande+"\r\n").encode())
ConnexionSecurise.close()
