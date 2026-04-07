#

def chiff_Cesar(txt, K):
    n = len(txt)
    k = ord(K) -ord('A')
    new_txt = ""
    for i in range(n):
        if txt[i].isalpha():
            x = ord(txt[i].upper()) - ord('A')  # lettre → nombre
            y = (x + k) % 26                     # décalage
            new_txt += chr(y + ord('A'))          
        else:
            new_txt += txt[i]  
    return new_txt

def dechiff_Cesar(txt, K):
    n = len(txt)
    k = ord(K) -ord('A')
    old_txt = ""
    for i in range(n):
        if txt[i].isalpha():
            x = ord(txt[i].upper()) - ord('A')  # lettre → nombre
            y = (x - k) % 26                     # décalage
            old_txt += chr(y + ord('A'))          
        else:
            old_txt += txt[i]
    return old_txt

def afficher_chiff(old,new,dechiff = False):
    n = len(old)
    if dechiff :
        print(" "*(n-4), "Dechiffrement:")
    else:    
        print(" "*(n-4), "Chiffrement:")
    print('=' * (n*2+8))  
    print(f"| {old} --> {new}|")
    print('=' * (n*2+8))


if __name__ == "__main__":
    #===Lettre Claire===
    txt = "CHIFFRE DE CESAR"

    #---Cesar---
    new = chiff_Cesar(txt,'B')
    afficher_chiff(txt,new)
    afficher_chiff(new,dechiff_Cesar(new,'B'),True)
    

#  ==================================
#  Chiffrement : y = (x + K) mod 26
#  Déchiffrement : x = (y - K) mod 26
#  ==================================

# ============================================================
# Exercice 1 - Question 2 : Attaque par FORCE BRUTE
# ============================================================

# On essaie les 26 décalages possibles (K=0 à K=25) :

# K=0  → gvctx skveq qi
# K=1  → fubsw rjudp ph
# K=2  → every night is  ✅ LISIBLE !
# K=3  → dudqx mhfgs hr
# ...

# K=2 donne "every night is" qui est lisible
# donc la clé est C (3ème lettre = décalage 2)


# ============================================================
# Exercice 1 - Question 3 : Attaque par ANALYSE FRÉQUENTIELLE
# ============================================================

# Étape 1 : on compte les lettres du texte "gvctx skveq qi"
# g=1, v=2, c=1, t=1, x=1, s=1, k=1, e=1, q=2, i=1

# Étape 2 : la lettre la plus fréquente est 'v' (ou 'q') avec 2 occurrences

# Étape 3 : on suppose que 'v' correspond à 'e' en français
# décalage = position(v) - position(e) = 21 - 4 = 17

# Étape 4 : on déchiffre avec K=17 → résultat ILLISIBLE ❌

# ⚠️ DISCUSSION :
# L'analyse fréquentielle échoue ici car le texte est trop court (12 lettres)
# La distribution des lettres ne représente pas les vraies fréquences du français
# Sur un texte de plusieurs centaines de lettres, cette méthode serait efficace
# Ici, la force brute reste la meilleure approche