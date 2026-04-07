from Bissection import *
from PointFixe import *
from Newton import *
def menu():
    print("+======Menu:======+")
    print("|  1-Dichotomie   |\n|  2-Point Fixe   |\n|  3-Newton       |\n|  0-Quitter      |")  
    print("+=================+")
def submenu():
    print("+================+")
    print("|  1-Iterative   |\n|  2-Recursive   |\n|  0-Retour      |")  
    print("+================+")

# ------------------------------------------------
# Fonction f(x) Doit Etre Changé dans 'Fonction.py'
# ------------------------------------------------

# Initialisation 
a,b = 1,2
x0 = 1.5

if __name__ == "__main__":
    eps = float(input("ε = "))
    while True:
        menu()
        option = int(input("Entrez une methode:"))
        if option == 1:
            while True:
                submenu()
                suboption = int(input("Entrez une option:"))
                if suboption == 1:
                    racine_dichotomie(a,b,eps)
                elif suboption == 2:
                    racine_dichotomie_rec(a,b,eps)
                else:
                    break
        elif option ==2:
            while True:
                submenu()
                suboption = int(input("Entrez une option:"))
                if suboption == 1:
                    racine_point_fixe(a,b,x0,eps)
                elif suboption == 2:
                    racine_point_fixe_rec(a,b,x0,eps)
                else:
                    break
        elif option == 3:
            while True:
                submenu()
                suboption = int(input("Entrez une option:"))
                if suboption == 1:
                    racine_newton(a,b,x0,eps)
                elif suboption == 2:
                    racine_newton_rec(a,b,x0,eps)
                else:
                    break
            
        else:
            print("+=================+")
            print("| Session Terminé |")
            print("+=================+")
            break