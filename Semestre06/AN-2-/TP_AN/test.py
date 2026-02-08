import sympy as sp
from colorama import Fore,Style 

def polynome_lagrange(points):
    x = sp.Symbol('x')
    n = len(points) - 1
    pol = 0
    for i in range(n):
        l_i = 1
        for j in range(n):
            if j != i:
                if points[i][0] - points[j][0]:
                    l_i *= (x - points[j][0])/(points[i][0] - points[j][0]) 
        pol += points[i][1] * l_i # Pi = yi * Li
    pol = sp.simplify(pol)
    return pol
def polynome_newton(points):
    pol = 0

    return pol
if __name__ == "__main__":
    points = [(0,0),(1,3),(3,1),(5,2),(8,2)]
    P = polynome_lagrange(points)
    print(Fore.YELLOW,"* Polynome de Lagrange: \n  ",Fore.GREEN,"P(x) = ",P ,Style.RESET_ALL)
    
