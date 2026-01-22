def menu():
    print("+-----Menu Principal:------+")
    print("| 1-Lire Systeme (A|b)     |\n| 2-Afficher Systeme (A|b) |\n| 0- Quitter.              |")  
    print("+--------------------------+")
def submenu():
    print("1-Itérative.\n2-Récursive.\n0-Retour.")
def menu_cri_arret():
    print("+-----------Critère d'arret:------------+")
    print(" 1-Nombre d'itération.\n 2-Epsilon.\n 0-Retour")
def lire_systeme(a,b):
    n = len(a)
    lire_matrice(a,n,n)
    for i in range(0,n):
        b[i] = int(input(f"B{i+1}="))

if __name__ == "__main__":
    while True:
        menu()
        option = int(input("Entrez une option:"))
        if option == 1:
            n = int(input("Entrez la taille de la matrice carré:"))
            t = [[0 for j in range(0,n)] for i in range(0,n)]
            v = [0] * n
            lire_systeme(t,v)
            a = [x[:] for x in t]
            b = v[:]
        elif option ==2:
            print("+-----------(A|b)----------+")
            afficher_systeme(t,v)
            print("+--------------------------+")
            print()
        elif option == 3:
                a = [x[:] for x in t]
                b = v[:]
        else:
            print("+-----------------+")
            print("| Session Terminé |")
            print("+-----------------+")