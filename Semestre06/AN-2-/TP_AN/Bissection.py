import sympy as sp
from contextlib import redirect_stdout

x = sp.Symbol('x')
f = x**3 +4 * x**2 - 10 # f(x)
a,b = 1,2 # x: [1,2] 

    
def n_iteration(a,b,eps): 
        return sp.log((b-a)//eps)/sp.log(2)  # n >= [ln((b-a)/eps)/ln(2)]-1    
def racine_dichotomie(f,a,b,eps):
    f_a = f.subs(x,a)
    f_b = f.subs(x,b)
    if f_a * f_b > 0 :
        print("On ne Peut pas résoudre avec dichotomie!")
        return
    # ---Functions---
    def draw_line():
        for _ in range(m):
            print("+",end="")
            for __ in range(max_width+1):
                print("-",end="")
        print("+")
    #-----Affichage-----
    signe= "-"
    k = 0
    t = [k,a,(a+b)/2,b,signe,b-a]
    x_char = ['N','A','C','B','Signe','B - A']
    m = len(x_char)
    max_width = max(max([(len(f"{t[i]:.4f}")) for i in range(m) if i != m-2]),5) # Pour Eviter le décalage (5 est la taille de la chaine 'signe')
    # Etat Initial
    print(" "* m*2 ,"Dichotomie:")
    draw_line()
    for i in range(m):    
        print(f"| {x_char[i]:>{max_width-1}}" ,end=" ")
    print("|")
    draw_line()
    while b-a > eps: # Racine Existe
        c = (b+a)/2
        f_a = f.subs(x,a)
        f_c = f.subs(x,c)
        if f_a * f_c < 0:
            b = c
            signe = "-"
        else : 
            a = c
            signe = "+" 

        t = [k,a,c,b,signe,b-a]

        
        print(f"|{t[0]:>{max_width}} ",end="")   
        for j in range(1,m):
            if isinstance(t[j],str):
                print(f"|{t[j]:>{max_width}}",end=" ")
            else:
                print(f"| {t[j]:>{max_width}.4f}",end="")    
        print("|")
        draw_line()
        t = [] ; k = k+1

if __name__ == '__main__':
    with open ('output1.txt','w') as file:
        with redirect_stdout(file):
            racine_dichotomie(f,1,2,1e-3)