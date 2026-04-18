# =================================
# |  TP8 : Integration Numérique  |
# |  Nom:    BELKASMI             |
# |  Prénom: Abdeldjalil          |
# |  ING3 - IA                    |
# =================================

from Rectangle import *
from Trapeze import *
from Simpson import *

def menu():
    print("+==========Menu:==========+")
    print("| 1-Lire Les Données      |\n"
          "| 2-Methode des Rectangles|\n"
          "| 3-Methode des Trapezes  |\n"
          "| 4-Methode Simpson       |\n"
          "| 0-Quitter               |")  
    print("+=========================+")
def menu_rect():
    print("+========================+")
    print("| 1- Rectangles a gauche |\n"
          "| 2- Rectangle a droite  |\n"
          "| 3- Rectangle au milieu |\n"
          "| 4- Erreur Absolue      |\n"
          "| 5 -Borne D'erreur      |\n"
          "| 0- Retour              |")  
    print("+=========================+")
def submenu(Rec = False):
    if Rec:            
        print("+===================+")
        print("|  1-Iterative      |\n"
              "|  2-Recursive      |\n"
              "|  0-Retour         |")  
        print("+===================+")
    else:
        print("+===================+")
        print("|  1-Iterative      |\n"
            "|  2-Recursive      |\n"
            "|  3-Erreur Absolue |\n"
            "|  4-Borne D'erreur |\n"
            "|  0-Retour         |")  
        print("+==================+")

# Les Données Sont declarés ici Mais peuvent etre changer dans le menu 
# (Option 1)
 
# ===
a = 1
b = 2
n = 4
# ===

# --- Main ---
if __name__ == "__main__":
    while True:
        menu()
        option = int(input("Choisissez une méthode:"))
        if option == 1:
            a = int(input("*   a = "))
            b = int(input("**  b = "))
            n = int(input("*** N = "))
        elif option == 2:
            while True:
                menu_rect()
                option_rect = int(input("//-->"))
                if option_rect == 1:
                    while True :
                        submenu(True)
                        suboption = int(input("Choisissez une option:"))
                        if suboption == 1 :
                            print(f"* Gauche : ∫f(x) dx = {rectangle_gauche_recursive(a,b,n):.4f}")
                        elif suboption ==2:
                            print(f"* Gauche Rec: ∫f(x) dx = {rectangle_gauche_recursive(a,b,n):.4f}")
                        else: break
                elif option_rect == 2:
                    while True:
                        submenu(True)
                        suboption = int(input("Choisissez une option: "))
                        if suboption == 1 :
                            print(f"* Droite : ∫f(x) dx = {rectangle_gauche_recursive(a,b,n):.4f}")
                        elif suboption ==2:
                            print(f"* Droite Rec: ∫f(x) dx = {rectangle_gauche_recursive(a,b,n):.4f}")
                        else: break
                elif option_rect == 3:
                    while True:
                        submenu(True)
                        suboption = int(input("Choisissez une option: "))
                        if suboption == 1:
                            print(f"* Milieu : ∫f(x) dx = {rectangle_gauche_recursive(a,b,n):.4f}")
                        elif suboption ==2:
                            print(f"* Milieu Rec: ∫f(x) dx = {rectangle_gauche_recursive(a,b,n):.4f}")
                        else: break
                elif option_rect ==4 :
                    I_ex = float(input("Entrer I exacte:"))
                    print(f"** |I - ∫f(x) dx| = ",erreur_absolue(I_ex,a,b,n))
                elif option_rect == 5:
                    print("*** Borne D'erreur = ",borne_erreur(a,b,n))
                else : break       
        elif option == 3:
            while True:
                submenu()
                suboption = int(input("Choisissez une option: "))
                if suboption == 1:
                    print(f"* Trapeze: ∫f(x) dx = {trapeze(a,b,n):.4f}")
                elif suboption == 2:
                    print(f"* Trapeze Rec: ∫f(x) dx = {trapeze(a,b,n):.4f}")
                elif suboption == 3 :
                    I_ex = float(input("Entrer I exacte:"))
                    print(f"** |I - ∫f(x) dx| = ",erreur_absolue_trapeze(I_ex,a,b,n))
                elif suboption == 4:
                    print("*** Borne D'erreur = ",borne_erreur_trapeze(a,b,n))
                else : break
        
        elif option == 4:
            while True :
                submenu()
                suboption = int(input("Choisissez une option: "))
                if suboption == 1:
                    print(f"* Simpson : ∫f(x) dx = {simpson(a,b,n):.4f}")
                elif suboption == 2:
                    print(f"* Simpson Rec: ∫f(x) dx = {simpson_recursive(a,b,n):.4f}")
                elif suboption == 3 :
                        I_ex = float(input("Entrer I exacte:"))
                        print(f"** |I - ∫f(x) dx| = ",erreur_absolue_simpson(I_ex,a,b,n))
                elif suboption == 4:
                        print("*** Borne D'erreur = ",borne_erreur_simpson(a,b,n))
                else : break
            
        else:
            print("+=================+")
            print("| Session Terminé |")
            print("+=================+")
            break
    