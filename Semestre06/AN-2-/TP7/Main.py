from Lagrange import *
from Newton import *

def menu():
    print("+==========Menu:==========+")
    print("|  1-Lire Point D'appui   |\n|  2-Afficher Point       |\n|  3-Lagrange             |" \
    "\n|  4-Newton               |\n|  0-Quitter              |")  
    print("+=========================+")
def submenu(Rec = True):
    if Rec:
        print("+===================+")
        print("|  1-Iterative      |\n|  2-Recursive      |\n|  3- Ajouter Point |\n|  0-Retour         |")  
        print("+===================+")
    else :
        print("+====================+")
        print("|  1-Calcul Polynome |\n|  2-Ajouter Point   |\n|  0-Retour          |")  
        print("+====================+")     
def afficher_points(points):
    X = [] ; Y = []
    for x_i,y_i in points:
        X.append(x_i)
        Y.append(y_i)
    n = len(points)
    #-----Affichage-----
    max_width = max(max([len(f"{X[i]:.4f}") for i in range(n)]),
                    max([len(f"{Y[i]:.4f}") for i in range(n)]))
    x_char = ['X'] + [f"{X[i]:.3f}" for i in range(n)]
    y_char = ['Y'] + [f"{Y[i]:.3f}" for i in range(n)]
    m = len(x_char)

    def draw_line():
        for _ in range(m):
            print("+",end="")
            for __ in range(max_width+1):
                print("-",end="")
        print("+")

    # Etat Initial
    draw_line()
    for i in range(m):
        print(f"|{x_char[i]:>{max_width}} ",end="")
    print("|")
    draw_line()
    for i in range(m):
        print(f"|{y_char[i]:>{max_width}} ",end="")
    print("|")
    draw_line()

if __name__ == "__main__":
    points = []
    while True:
        menu()
        option = int(input("Choisissez une méthode:"))
        if option == 1:
            n = int(input("Nombre de Point:"))
            for i in range(n):
                x,y = map(float , input(f"Point {i} = ").split())
                points.append((x,y))
        elif option == 2:
            afficher_points(points)
        elif option ==3:
            while True:
                submenu(False)
                suboption = int(input("entrez une option:"))
                if suboption == 1:
                    v = float(input("X = "))
                    print(f"L({v}) = {interpolation_lagrange(points,v,n):.4f}")
                elif suboption == 2:
                    x,y = map(float , input(f"Point {len(points) +1} = ").split())
                    points.append((x,y))
                else:
                    break
        elif option == 4:
            submenu()
            while True:
                suboption = int(input("entrez une option:"))
                if suboption == 1:
                    v = float(input("X = "))
                    print(f"N({v}) = {interpolation_newton(points,v):.4f}")  
                elif suboption == 2:
                    v = float(input("X = "))
                    print("---Newton_Recursive---")
                    print(f"    N({v}) = {interpolation_newton_rec(points,v):.4f}")  
                elif suboption == 3:
                    x,y = map(float , input(f"Point {len(points) +1} = ").split())
                    points.append((x,y))
                else:
                    break     
        else:
            print("+=================+")
            print("| Session Terminé |")
            print("+=================+")
    