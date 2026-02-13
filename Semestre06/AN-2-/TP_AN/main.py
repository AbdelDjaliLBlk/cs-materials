def menu():
    print("+-----Menu Principal:------+")
    print("| 1-Lire Systeme (A|b)     |\n| 2-Afficher Systeme (A|b) |\n| 0- Quitter.              |")  
    print("+--------------------------+")
def submenu():
    print("1-Itérative.\n2-Récursive.\n0-Retour.")


if __name__ == "__main__":
    while True:
        menu()
        option = int(input("Entrez une option:"))
        if option == 1:
            print()
        elif option ==2:
            print()
        elif option == 3:
            print()
        else:
            print("+-----------------+")
            print("| Session Terminé |")
            print("+-----------------+")