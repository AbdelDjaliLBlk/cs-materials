# +----------------------+
# |  Nom: Belkasmi       |
# |  Prenom: Abdeldjalil |
# |  Promo: ING 3 -IA-   |
# +----------------------+

from Base_functions import *
from Cramer import *
from Gauss import *
from Gauss_partiel import *
from Gauss_total import *
from Decomposition_Lu import *
from Gauss_jordan import *
from Jacobi import *
from Gauss_seidel import *

def menu():
    print("+-----Menu Principal:------+")
    print("| 1-Lire Systeme (A|b)     |\n| 2-Afficher Systeme (A|b) |\n| 3-Méthodes directs.      |\n| 4-Méthodes itératives.   |\n| 0- Quitter.              |")  
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
            while True :
                a = [x[:] for x in t]
                b = v[:]
                print("+----Méthodes directes-----+")
                print("| 3.1-Cramer.              |\n| 3.2-Gauss_Pivot Non Nul. |\n| 3.3-Gauss_Pivot Partiel. |\n| 3.4-Gauss_Pivot Total.   |")
                print("| 3.5-Décomposition LU.    |\n| 3.6-Gauss_Jordan.        |\n| 0.0- Retour.             |")
                print("+--------------------------+")
                choix = int(input("Choisissez une méthode direct de résolution: "))
                if choix == 1:
                    suboption = -1
                    while suboption != 0:
                        a = [x[:] for x in t]
                        b = v[:]
                        submenu()
                        suboption = int(input("Choisissez une méthode de résolution : "))
                        if suboption == 1:
                            print("+------Cramer------+")
                            x = cramer(a,b)
                            for i in range(n):
                                print(f"|  x{i+1} = {x[i]:.4f}")
                            print("+------------------+")  
                        elif suboption == 2:
                            x = [0] * n
                            det = det_rec(a)
                            if det != 0:
                                cramer_rec(a,[row[:] for row in a],b,x,0,0,n,det)
                                print("+---Cramer Rec---+")
                                for i in range(n):
                                    print(f"|  x{i+1} = {x[i]:.4f}")
                                print("+----------------+")
                            else:
                                print("+---------Warning:---------+")
                                print("|      Determinant = 0     |")
                                print("+--------------------------+")                        
                elif choix == 2:
                    suboption = -1
                    while suboption != 0:
                        a = [x[:] for x in t]
                        b = v[:]
                        submenu()
                        suboption = int(input("Choisissez une méthode de résolution : "))
                        if suboption == 1:
                            pivot_gauss(a,b)
                            print("+------------Gauss:------------+")
                            print("-->Matrice réduite:")
                            afficher_systeme(a,b)
                            print("+------------------------------+")
                        elif suboption ==2:
                            pivot_gauss_rec(a,b,1,0,0,n)
                            print("+------------Gauss Récursif:------------+")
                            print("-->Matrice réduite:")
                            afficher_systeme(a,b)
                            print("-->Résolution donne : ",resolution_remontee(a,b))
                            print("+---------------------------------------+")
                elif choix == 3:
                    suboption = -1
                    while suboption != 0:
                        a = [x[:] for x in t]
                        b = v[:]
                        submenu()
                        suboption = int(input("Choisissez une méthode de résolution : "))
                        if suboption == 1:      
                            pivot_partiel(a,b)
                            print("+------------Pivot Gauss Partiel:------------+")
                            print("-->Matrice réduite:")
                            afficher_systeme(a,b)
                            print("+--------------------------------------------+")
                            print("-->Résolution donne : ",resolution_remontee(a,b))
                        elif suboption ==2:
                            print("+---------Pivot Gauss Partiel Récursif:---------+")
                            pivot_partiel_rec(a,b,n,0,0,0,0)
                            print("-->Matrice réduite:")
                            afficher_systeme(a,b)
                            print("+----------------------------------------+")
                elif choix == 4:
                    suboption = -1
                    while suboption != 0:
                        a = [x[:] for x in t]
                        b = v[:]
                        submenu()
                        suboption = int(input("Choisissez une méthode de résolution : "))
                        if suboption == 1:      
                            print("\n+------------Pivot Gauss Total:------------+")
                            pivot_total(a,b)
                            print("*** Matrice réduite:")
                            afficher_systeme(a,b)
                            print("+----------------------------------------+")
                        elif suboption ==2:
                            print("\n+---------Pivot Gauss Total Récursif:---------+")
                            x = [f"x{i+1}"for i in range(n)]
                            pivot_total_rec(a,b,n,0,0,0,0,x)
                            print("***Matrice réduite:")
                            afficher_systeme(a,b)
                            print("+----------------------------------------+")
                elif choix == 5:
                    suboption = -1
                    while suboption != 0:
                        a = [x[:] for x in t]
                        b = v[:]
                        submenu()
                        suboption = int(input("Choisissez une méthode de résolution : "))
                        if suboption == 1:      
                            decomposition_lu(a,b)
                            print(f"+----------------------------------------+")
                        elif suboption == 2:
                            l = matrice_identite(n)
                            if condition_lu(a,n) == False:
                                decomposition_lu_rec(a,b,l,n,1,0,0,0)
                                print("+----------------------------------------+")
                            else:
                                print("+------------Warning:------------+")
                                print("|  Décomposition LU n'existe pas |")
                                print("+--------------------------------+")
                            
                        a = [x[:] for x in t]
                        b = v[:]
                        
                elif choix == 6:
                    suboption = -1
                    while suboption != 0:
                        a = [x[:] for x in t]
                        b = v[:]
                        submenu()
                        suboption = int(input("Choisissez une méthode de résolution : "))
                        if suboption == 1:                 
                            print("+-------------Gauss Jordan:-------------+")
                            gauss_jordan(a,b)
                            print("+---------------------------------------+")
                        elif suboption == 2:
                            print("+---------Gauss Jordan Recursif:--------+")
                            I = matrice_identite(n)
                            gauss_jordan_rec(a,b,I,n,0,0,0,0)
                            print("+---------------------------------------+")
                else: 
                    break
        elif option == 4:
             while True :
                a = [x[:] for x in t]
                b = v[:]
                print("+---Méthodes itératives---+")
                print("|    4.1-Jacobi           |\n|    4.2-Gauss_Seidel     |\n|    0.0-Retour           |")
                print("+-------------------------+") 
                choix = int(input("Choisissez une méthode itérative de résolution: "))
                if choix == 1 :
                    menu_cri_arret()
                    cri_arr = int(input("Entrer le Critère D'arret : "))
                    if cri_arr == 1:
                        suboption = -1
                        while suboption != 0:
                            submenu()
                            suboption = int(input("Choisissez une méthode de résolution : "))
                            if suboption == 1:
                                k = 0
                                while k <= 0:
                                    k = int(input("k = "))
                                print("------------Jacobi:------------")
                                jacobi(a,b,k)
                                print(f"----------------------------------------")
                            elif suboption == 2:
                                k = 0
                                while k <= 0:
                                    k = int(input("k = "))
                                print("------------Jacobi Rec:------------")
                                x = [0] * n
                                jacobi_rec(a,b,n,x,x,0,0,k,1) 
                                print(f"----------------------------------------")           
                    elif cri_arr ==2:
                        suboption = -1
                        while suboption != 0:
                            submenu()
                            suboption = int(input("Choisissez une méthode de résolution : "))
                            if suboption == 1:
                                eps = float(input("ε = "))
                                print(f"+------------Jacobi ε = {eps}------------+")
                                jacobi_epsilon(a,b,eps)
                                print("+----------------------------------------+")
                            elif suboption == 2:
                                eps = float(input("ε = "))
                                print(f"+----------Jacobi Rec ε = {eps}----------+")
                                jacobi_epsilon_rec(a,b,n,[0.0]*n,[0.0]*n,0,0,eps,eps+1)
                                print("+----------------------------------------+")
                                 
                elif choix == 2 :
                    menu_cri_arret()
                    cri_arr = int(input("Entrer le Critère D'arret : "))
                    if cri_arr == 1:
                        suboption = -1
                        while suboption != 0:
                            submenu()
                            suboption = int(input("Choisissez une méthode de résolution : "))
                            if suboption == 1:
                                k = 0
                                while k <= 0:
                                    k = int(input("k = "))
                                print("+------------Gauss-Seidel:-----------+")
                                gauss_seidel(a,b,k)
                                print("+------------------------------------+")
                            elif suboption == 2:
                                k = 0
                                while k <= 0:
                                    k = int(input("k = "))
                                print("+-------Gauss-Seidel-Recursif:-------+")
                                gauss_seidel(a,b,k)
                                print("+------------------------------------+")
                                
                            
                    elif cri_arr == 2:
                        suboption = -1
                        while suboption != 0:
                            submenu()
                            suboption = int(input("Choisissez une méthode de résolution : "))
                            if suboption == 1:
                                eps = float(input("ε = "))
                                print(f"+-------Gauss-Seidel ε = {eps}-----------+")
                                gauss_seidel_epsilon(a,b,eps) 
                                print("+----------------------------------------+")
                            elif suboption ==2:
                                eps = float(input("ε = "))
                                print(f"+---Gauss-Seidel-Recursif ε = {eps}---+")
                                if not diagonale_dominante(a):
                                    print("+------------Warning:------------+")
                                    print("|     Diagonale non_dominante    |")
                                    print("+--------------------------------+")
                                else:
                                    gauss_seidel_epsilon_rec(a,b,n,[0.0]*n,[0.0]*n,0,0,eps,eps+1) 
                                    print("+-------------------------------------+")
                                
                else:
                    break

        else:
            print("+-----------------+")
            print("| Session Terminé |")
            print("+-----------------+")
            break