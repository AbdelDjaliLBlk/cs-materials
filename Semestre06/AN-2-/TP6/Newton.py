import math
from Fonction import *

def racine_newton(a,b,x0,ε):
    if x0 > b or x0 < a:
        print(f"{x0} not in [{a},{b}].")
        return
    # ---Functions---
    def draw_line():
        for _ in range(m):
            print("+",end="")
            for __ in range(max_width+1):
                print("-",end="")
        print("+")
    #-----Affichage-----
    k = 1
    t = [k, x0, x0 - f_x(x0)/df_x(x0), abs(x0 - f_x(x0)/df_x(x0) - x0)]
    x_char = ['N','X(n)','X(n+1)','X(n+1)-X(n)']
    m = len(x_char)
    max_width = max(max((len(f"{t[i]:.4f}")) for i in range(m)),12)
    # Etat Initial
    draw_line()
    for i in range(m):    
        print(f"|{x_char[i]:>{max_width}} ",end="")
    print("|")
    draw_line()
    # Procedure Newton
    while True:
        X = x0 - f_x(x0)/df_x(x0)
        if (abs(X - x0) < ε): break
        t = [k, x0, X, abs(X - x0)]
        print(f"|{t[0]:>{max_width}}",end=" ")   
        for j in range(1,m):
            print(f"|{t[j]:>{max_width}.4f} ",end="")    
        print("|")
        draw_line()
        # Compteur à 0
        k += 1
        x0 = X
        t = []
    print(f"(Rec)--> x = {X:.4f}.")

def racine_newton_rec(a,b,x0,ε):
    if x0 > b or x0 < a:
        print(f"{x0} not in [{a},{b}].")
        return
    # ---Functions---
    def draw_line():
        for _ in range(m):
            print("+",end="")
            for __ in range(max_width+1):
                print("-",end="")
        print("+")
    def newton_recursive(x0,k):
        X = x0 - f_x(x0)/df_x(x0)
        if abs(X - x0) < ε: # Racine Existe
            print(f"--> x = {X:.4f}.")
            return X
        t = [k, x0, X, abs(X - x0)]
        print(f"|{t[0]:>{max_width}}",end=" ")   
        for j in range(1,m):
            print(f"|{t[j]:>{max_width}.4f} ",end="")    
        print("|")
        draw_line()
        # Compteur à 0
        return newton_recursive(X,k+1)
    #-----Affichage-----
    k = 1
    t = [k, x0, x0 - f_x(x0)/df_x(x0), abs(x0 - f_x(x0)/df_x(x0) - x0)]
    x_char = ['N','X(n)','X(n+1)','X(n+1)-X(n)']
    m = len(x_char)
    max_width = max(max((len(f"{t[i]:.4f}")) for i in range(m)),12)
    # Etat Initial
    draw_line()
    for i in range(m):    
        print(f"|{x_char[i]:>{max_width}} ",end="")
    print("|")
    draw_line()
    newton_recursive(x0,k)