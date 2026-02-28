import math
from Fonction import *

def racine_newton(a,b,x0,eps):
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
    x_n = g_x(x0)
    k = 1
    t = [k,x0,x_n,abs(x_n-x0)] 
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
        #X = ??
        if (abs(x_n - x0) < eps): break
        # T = []
        # .............
        print(f"|{t[0]:>{max_width}}",end=" ")   
        for j in range(1,m):
            print(f"|{t[j]:>{max_width}.4f} ",end="")    
        print("|")
        draw_line()
        # Compteur à 0
        k = k+1
        t = []
    print(f"--> x = {x_n:.4f}.")

if __name__ == '__main__':
    racine_newton(1,2,1.5,1e-3)