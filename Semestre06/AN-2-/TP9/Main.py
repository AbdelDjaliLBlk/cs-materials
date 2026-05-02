# =================================
# |  TP9: Equation Differentielle |
# |  Nom:    BELKASMI             |
# |  Prénom: Abdeldjalil          |
# |  ING3 - IA                    |
# =================================

# ====================================
# |           REMARQUE               |
# |  La Fonction Peut Etre Change    |
# |  Depuis le Fichier 'Fonction.py' |
# ====================================

from Euler import *
from Euler_Mod import *
from Taylor import *
from Range_Kutta_4 import *
from Point_Milieu import *

def menu():
    print("+==========Menu:==========+")
    print("| 1-Methode Euler         |\n"
          "| 2-Methode Euler Modifie |\n"
          "| 3-Methode Taylor        |\n"
          "| 4-Methode Point Milieu  |\n"
          "| 5-Methode RK4           |\n"
          "| 0-Quitter               |")  
    print("+=========================+")
def submenu():               
    print("+===================+")
    print("|  1-Iterative      |\n"
          "|  2-Recursive      |\n"
          "|  0-Retour         |")  
    print("+===================+")
    
# --- Main ---
if __name__ == "__main__":
    print(" === Résolution d'équation différentielle ===")
    while True:
        menu()
        option = int(input("Votre Choix :"))
        if option == 1:
            while True:   
                    submenu()
                    suboption = int(input("Choisissez une option:"))
                    if suboption == 1:
                        print(" === Euler ===")  
                        euler(f, 0, 1, 0.1, 10, y_exact=y_exact)
                    elif suboption == 2:
                        print(" === Euler Recursive===")
                        euler_rec(f, 0, 1, 0.1, 10, y_exact=y_exact)
                    else: break
                
        elif option == 2:
            while True:   
                submenu()
                suboption = int(input("Choisissez une option:"))
                if suboption == 1 :
                    print(" === Euler Modifie ===")
                    euler_mod(f, 0, 1, 0.1, 10, y_exact=y_exact)
                elif suboption ==2:
                    print(" === Euler Modifie Rec ===")
                    euler_mod_rec(f, 0, 1, 0.1, 10, y_exact=y_exact)
                else: break
            
        elif option == 3:
            while True:
                submenu()
                suboption = int(input("Choisissez une option: "))
                if suboption == 1:
                    print(" === Taylor ===")
                    taylor(f, dfdx, dfdy, 0, 1, 0.1, 10, y_exact=y_exact)
                elif suboption == 2:
                    print(" === Taylor Recursive ===")
                    taylor_rec(f, dfdx, dfdy, 0, 1, 0.1, 10, y_exact=y_exact)
                else : break

        elif option == 4:
            while True :
                submenu()
                suboption = int(input("Choisissez une option: "))
                if suboption == 1:
                    print(" === Point Milieu ===")
                    point_milieu(f, 0, 1, 0.1, 10, y_exact=y_exact)
                elif suboption == 2:
                    print(" === Point Milieu Rec ===")
                    point_milieu_rec(f, 0, 1, 0.1, 10, y_exact=y_exact)
                else : break

        elif option == 5:
            while True :
                submenu()
                suboption = int(input("Choisissez une option: "))
                if suboption == 1:
                    print(" === RK4 ===")
                    RK4(f, 0, 1, 0.1, 10, y_exact=y_exact) 
                elif suboption == 2:
                    print(" === RK4 Recursive ===")
                    RK4_rec(f, 0, 1, 0.1, 10, y_exact=y_exact)
                else : break
        else:
            print("+=================+")
            print("| Session Terminé |")
            print("+=================+")
            break
    