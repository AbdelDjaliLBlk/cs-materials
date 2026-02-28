from Bissection import *
from PointFixe import *
from Newton import *
def menu():
    print("+======Menu:======+")
    print("|  1-Dichotomie   |\n|  2-Point Fixe   |\n|  3-Newton       |\n|  0-Quitter      |")  
    print("+=================+")

# ------------------------------------------------
# Fonction f(x) Doit Etre Changé dans 'Fonction.py'
# ------------------------------------------------

# Initialisation 
a,b = 1,2
eps = 1e-3
x0 = 1.5

if __name__ == "__main__":
    while True:
        menu()
        option = int(input("Entrez une option:"))
        if option == 1:
            racine_dichotomie(a,b,eps)
        elif option ==2:
            racine_point_fixe(a,b,x0,eps)
        elif option == 3:
            racine_newton(a,b,x0,eps)
        else:
            print("+=================+")
            print("| Session Terminé |")
            print("+=================+")