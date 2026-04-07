import math
from Fonction import *

def n_iteration(x0,x1,k,eps): 
        return math.ln(((1-k)*eps)/math.abs(x1-x0))/math.ln(k)  # n >= [ln((1-k)*eps) /|x1-x0|)/ln(k)]    
def racine_point_fixe(a,b,x0,eps):
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
    # Procedure Point Fixe
    while True:
        x_n = g_x(x0)
        if (abs(x_n - x0) < eps): break
        t = [k,x0,x_n,abs(x_n - x0)]
        print(f"|{t[0]:>{max_width}}",end=" ")   
        for j in range(1,m):
            print(f"|{t[j]:>{max_width}.4f} ",end="")    
        print("|")
        draw_line()
        x0 = x_n 
        k = k+1
        t = []
    print(f"(Rec)--> x = {x0:.4f}.")
def racine_point_fixe_rec(a,b,x0,eps):
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
    def point_fixe_recursive(x0,k):
        x_n = g_x(x0)
        if abs(x_n - x0) < eps: # Racine Existe
            print(f"--> x = {x0:.4f}.")
            return x0
        t = [k,x0,x_n,abs(x_n - x0)]
        print(f"|{t[0]:>{max_width}}",end=" ")   
        for j in range(1,m):
            print(f"|{t[j]:>{max_width}.4f} ",end="")    
        print("|")
        draw_line()
        # Procedure Point Fixe
        return point_fixe_recursive(x_n,k+1)
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
    point_fixe_recursive(x_n,k)