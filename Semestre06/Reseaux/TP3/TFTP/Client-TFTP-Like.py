import socket

ClientSocket = socket.socket()
host = "145.220.21.40"
port = 9500

print("Connexion au serveur {}:{}".format(host, port))
ClientSocket.connect((host, port))


print("Connecte au serveur !")
print("=" * 40)
print("Commandes disponibles :")
print("  2:         --> Lister les fichiers")
print("  1:NomFichier --> Telecharger un fichier")
print("  3:NomDossier --> Changer de repertoire")
print("  0:bye        --> Quitter")
print("=" * 40)


def recevoir_reponse(socket_client):
    reponse = b""  # Buffer pour stocker les octets recus
    
    while True:
        morceau = socket_client.recv(4096)
        
        if len(morceau) == 0:
            break
        reponse += morceau
        
        if b"--\r\n\r\n" in reponse:
            break
    
    return reponse.replace(b"--\r\n\r\n", b"").decode("utf-8", errors="replace")

while True:
    try:
        commande = input("\nEntrez votre commande : ").strip()
        if not commande:
            print("Commande vide, reessayez.")
            continue
        if ":" not in commande:
            print("Format invalide ! Utilisez : TypeCommande:Argument")
            print("Exemple : 1:fichier.txt  ou  2:  ou  3:dossier  ou  0:bye")
            continue
        
        parties = commande.split(":")
        type_commande = parties[0]
        
        if type_commande not in ["0", "1", "2", "3"]:
            print("Type de commande invalide ! Utilisez 0, 1, 2, ou 3")
            continue

        ClientSocket.send(commande.encode("utf-8"))

        reponse = recevoir_reponse(ClientSocket)
        print("\n--- Reponse du serveur ---")
        print(reponse)
        print("--------------------------")
        
        if type_commande == "0":
            print("Deconnexion du serveur.")
            break

        if type_commande == "1":
            nom_fichier = parties[1] if len(parties) > 1 else ""
            
            if nom_fichier and reponse and not reponse.startswith("500") and not reponse.startswith("501"):
                try:
                    with open(nom_fichier, "wb") as fichier_local:
                        fichier_local.write(reponse.encode("utf-8"))
                    print("Fichier '{}' sauvegarde avec succes !".format(nom_fichier))
                except Exception as e:
                    print("Erreur lors de la sauvegarde : {}".format(e))
    
    except ConnectionResetError:
        print("Erreur : Le serveur a ferme la connexion.")
        break
    
    except ConnectionAbortedError:
        print("Erreur : Connexion interrompue.")
        break
    
    except KeyboardInterrupt:
        print("\nInterruption par l'utilisateur.")
        try:
            ClientSocket.send(b"0:bye")
        except:
            pass
        break
    
ClientSocket.close()
