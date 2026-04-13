Oreginal=open(input("Entrez le chemin de votre fichier :"),'rb')
Copie=open(input("Entrez l'enmplacement de la copie :") ,"wb")
Copie.write(Oreginal.read())
Copie.close()
