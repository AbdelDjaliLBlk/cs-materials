from simplex import calcul_zj,variable_entrante,variable_sortante
from sympy import symbols,Expr
from contextlib import redirect_stdout

# Min Z = 5x + 10y
# 6x + 2y ≥ 36
# 5x + 5y ≥ 50
# x ≥ 0 ;  y ≥ 0 

M = symbols('M',positive = True)
a = [   [0,0,5,10,0,0,M,M,0],#Cj
        [M,36,6,2,-1,0,1,0,0],#A1
        [M,50,5,5,0,-1,0,1,0],#A2
        [0,0,0,0,0,0,0,0,0],#Zj
        [0,0,5,10,0,0,0,0,0]#Cj-Zj
        ]

def afficher_simplexe_vArt(a, titre="Simplexe Variable Artificielle",v_ent=None, i_ent=None, j_ent=None):
    n = len(a)
    m = len(a[0])

    def cell_str(x):
        return f"{x:.2f}" if not isinstance(x, Expr) else str(x)
    
    max_width = max(len(cell_str(a[i][j])) for i in range(n) for j in range(m))
    legend_width = max(len(str(l)) for l in legend)

    if v_ent is not None:
        legend[i_ent] = v_ent
        a[i_ent][0] = a[0][j_ent]

    print("   " * m + titre)
    def draw_line_vArt():
        print(
            "+"
            + "-" * (max_width) + "+"
            + "-" * (legend_width+2) + "+"
            + "+".join("-" * (max_width+1) for _ in range(m-1))
            + "+"
        )

    draw_line_vArt()

    for i in range(n):
        s = cell_str(a[i][0])
        print(f"|{s:>{max_width-1}} ", end="")
        print(f"| {legend[i]:>{legend_width}}", end=" |")

        for j in range(1, m):
            s = cell_str(a[i][j])
            print(f"{s:>{max_width}}", end=" |")

        print()
        draw_line_vArt()
def legend_simplex_vArt(a,min = 0):
    legend = [] 
    legend.append("Cj")
    for i in range(len(a)-3):
        legend.append(f"A{i+1}")
    legend.append("Zj")
    if min != 0 :
        legend.append("Zj-Cj")
    else:
        legend.append("Cj-Zj")
    
    return legend
def simplexe_vArt(a):
    calcul_zj(a)
    afficher_simplexe_vArt(a)
    while True:
        j_p = variable_entrante(a)
        n = len(a)
        m = len(a[0])    
       
        if all(a[n-1][j] <= 0 for j in range(2,m-1)):
            print("Solution optimale atteinte")
            v_max = max(a[n-2][j] for j in range(1,m-1))
            print("Z* = ",v_max)
            break
        for i in range(1,n-2):
            a[i][m-1] = 0

        i_p = variable_sortante(a, j_p)
        pivot = a[i_p][j_p]
        afficher_simplexe_vArt(a, "Choix Pivot",f"X{i_p}",i_p,j_p)
       
        print(f"* Max = {a[n-1][j_p]}")
        print(f"** Min = {a[i_p][m-1]}")
        print(f"*** Pivot (A[{i_p}][{j_p}]) = {pivot:.2f}")
       
        for j in range(1, m-1):
            a[i_p][j] /= pivot
        for i in range(1, n-2):
            if i != i_p:
                facteur = a[i][j_p]
                for j in range(1, m-1):
                    a[i][j] -= facteur * a[i_p][j]
        calcul_zj(a)
        afficher_simplexe_vArt(a, "Apres Elimination",f"X{i_p}",i_p,j_p)

legend = legend_simplex_vArt(a,1)
if __name__ == "__main__":
    with open("simplexArt.txt", "w") as f:
        with redirect_stdout(f):
            afficher_simplexe_vArt(a,"Forme Standard")    
            calcul_zj(a,1)
            afficher_simplexe_vArt(a,"--------------")