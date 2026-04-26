# code python 3
def Decode64bits(_4Octets_lu):
    # prendre en parametre 4octets (4 caracteres)
    global FichierDecode # variable globale
    
    Sequence_4Octets=_4Octets_lu
    ValeurBinaire=""
    # si la sequence de caractere contient "=" alors celle-ci marque la fin du fichier
    if("=" in Sequence_4Octets):
        # elimine les caractere "=" a la fin de la sequence
        Sequence_4Octets=Sequence_4Octets[:Sequence_4Octets.find("="):]
       
    for octet_indx in range(len(Sequence_4Octets)):
        # convertir le caractere a ca representation 64bits et ensuite vers ca representation binaire
        binval=bin(ConvertirCaracter64bits(Sequence_4Octets[octet_indx]))[2::]
        # complete la representation binaire par des 0s a gauche (pour avoir une representation 6bits)
        binval="0"*(6-len(binval))+binval
        ValeurBinaire+=binval
    
    for Threebits_char in range(0,len(ValeurBinaire),8):
        if(Threebits_char+8>len(ValeurBinaire)):
            break
        # pour toutes les sequence de 8 bits dans ValeurBinaire
        # obtenir le caractere 8bits correspandant
        CaractereASCII8bits=chr( int("0b"+ValeurBinaire[Threebits_char:Threebits_char+8:],0) )
        #print (CaractereASCII8bits.encode(),ord(CaractereASCII8bits))
        # enregistrer le caractere sur fichier
        FichierDecode.write(bytes([ord(CaractereASCII8bits)]))
    L=len(ValeurBinaire)
    # s'il reste des bits supplementaires
    if(L%8!=0):
        # si la sequence de bits ne contient pas que des 0
        if("0"*(L%8)!=ValeurBinaire[L-L%8::]):
            # complete la representation par des 0 a droit
            CaractereASCII8bits=chr( int("0b"+ValeurBinaire[L-L%8::]+(8-L%8)*"0",0) )
            
            # enregistrer le caractere sur fichier
            FichierDecode.write(bytes([ord(CaractereASCII8bits)]))

    #fin de la procedure Decode64bits
    
# si le caractere n'appartient pas a [A..Z, a..z, 0..9, +, / , =], supprimer le caratere
def SupprimerCaracteresSupplementaires(Contenu):
    Contenucleaned=""
    for octet in Contenu :
        caractere=(chr(octet))
        if(caractere>='A' and caractere<='Z'):
            Contenucleaned+=caractere
            continue
        if(caractere>='a' and caractere<='z'):
            Contenucleaned+=caractere
            continue
        if(caractere>='0' and caractere<='9' ):
            Contenucleaned+=caractere
            continue
        if(caractere=="+"):
            Contenucleaned+=caractere
            continue
        if(caractere=="/"):
            Contenucleaned+=caractere
            continue
        if(caractere=="="):
            Contenucleaned+=caractere
            
    return Contenucleaned # fin de la procedure SupprimerCaracteresSupplementaires
    
# obtient la representation 64bits du caractere
''' [A .. Z] = [0..25]
[a .. z] = [26..51]
[0..9]=[52..61]
"+" = 61
"/" = 62
"=" = 0 ( contrairement a A, les "=" sont ajoutes a la fin
pour que la taille de la chaine encdee soit un multiple de 4
'''
def ConvertirCaracter64bits(caractere):
    if(caractere>='A' and caractere<='Z'):
        return ord(caractere)-65
    if(caractere>='a' and caractere<='z'):
        return ord(caractere)-71
    if(caractere>='0' and caractere<='9' ):
        return ord(caractere)+4
    if(caractere=="+"):
        return 62
    if(caractere=="/"):
        return 63
    # le dernier cas correspond a "=" (si caractere=="=" return 0)
    return 0 # fin de la procedure ConvertirCaracter64bits

# lire le fichier qu'ont souhaite decoder
FichierEncode =open("MessageEncoder.txt",'rb')
# ouvrir le fichier dans le quel ont souhaite enregistrer le fichier decode
FichierDecode=open("MessageDecoder.png","wb")


Contenu=""
Contenu_Restant=""
# lire le fichier. Pour chaque morceau de d'octets
for Octets in FichierEncode:
    
    Contenu=Octets
    Contenu=SupprimerCaracteresSupplementaires(Contenu)
    Contenu=Contenu_Restant+Contenu    
    l=len(Contenu)
    Contenu_Restant=""
    # prendre une partie de la chaine de caratere avec une taille multiple de 4
    # si des caracteres supplementaires restent, on les garde dans le tompon "Contenu_Restant"
    if(l%4!=0):
        Contenu_Restant=Contenu[len(Contenu)-(l%4):len(Contenu):]
    if(len(Contenu)<4):
        continue
    
    PartieContenu_deTailleMultiple_de_4=l-(l%4)
    # appliquer le decodage sur chaque morceau de taille 4 caracteres
    for i in range(0,PartieContenu_deTailleMultiple_de_4,4):
        Decode64bits(Contenu[i:i+4:])
# fermeture du fichier de l'encodage
FichierDecode.close()
