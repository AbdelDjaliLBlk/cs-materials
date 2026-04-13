# Le programme suivant permet de copier un fichier en mode bynaire
# (exe, png, etc)

# Entrez le chemin de votre fichier a copier
Chemin_fichier_oreginal=input("Entrez le chemin de votre fichier :")
#Entrez le chemin de votre fichier :
Chemin_copie=input("Entrez l'enmplacement de la copie :")
# Ouverture du fichier en mode lecture (r) en octets (b)
Fichier_en_lecture=open(Chemin_fichier_oreginal,"rb")
# utilisez un chemin de fichier de votre choix
Suite_doctets=[]
print( "#"*20)
for bloque_octets in Fichier_en_lecture:
    Suite_doctets.append(bloque_octets)

# Ouverture du fichier en mode ecriture (w) en octets (b)
Fichier_en_ecriture=open(Chemin_copie,"wb")
for octets in Suite_doctets:
    # Ecriture de la suite d'octets dans le fichier Image
    Fichier_en_ecriture.write(octets)
# Fermeture du fichier
Fichier_en_ecriture.close()
