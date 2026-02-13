import sympy as sp
from colorama import Fore,Style 

# Declare Symbol X and The Points of f(x)
x = sp.Symbol('x')
points = [
    (100,10),
    (121,11),
    (144,12)
    ]

# Lagrange
def polynome_lagrange(points):
    n = len(points) 
    pol = 0
    for i in range(n):
        l_i = 1
        for j in range(n):
            if j != i:
                l_i *= (x - points[j][0])/(points[i][0] - points[j][0]) 
        pol += points[i][1] * l_i # Pi = yi * Li
    pol = sp.simplify(pol)
    return pol
def toString(P,values = None):
    print(Fore.YELLOW,"* Polynome de Lagrange: \n",Fore.GREEN,"-P(x)=",P ,Style.RESET_ALL,)
    if values: 
        print(Fore.YELLOW,"* Calculate:",Style.RESET_ALL)
        for v in values:
            print(f"  -P({Fore.LIGHTRED_EX}{v}{Style.RESET_ALL})= {Fore.LIGHTMAGENTA_EX}{float(P.subs(x,v)):.3f}.",Style.RESET_ALL)

# Newton
def polynome_newton(points):    
    pol = 0
    return pol

# Main
if __name__ == "__main__":
    P = polynome_lagrange(points)
    toString(P,[115,16])