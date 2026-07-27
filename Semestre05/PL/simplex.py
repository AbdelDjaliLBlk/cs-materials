from contextlib import redirect_stdout

#---------Simplexe---------
def afficher_simplexe(a,titre = "Simplexe Simple",v_ent = None,i_ent = None,j_ent = None):
    n = len(a)
    m  = len(a[0])
    max_width = max([(len(f"{a[i][j]:.2f}")) for i in range(n) for j in range(m)])
    legend_width = max([(len(f"{legend[i]}")) for i in range(len(legend))])
    
    if v_ent != None :
        legend[i_ent] = v_ent 
        a[i_ent][0] = a[0][j_ent]
    #-------Titre-------
    for space in range(m):
        print("   ",end="")
    print(titre)
    #-----Affichage-----
    def draw_line():
        for _ in range(m+1):
            print("+",end="")
            for __ in range(max_width+1):
                print("-",end="")
        print("+")
    draw_line()
    for i in range(n):
        print(f"|{a[i][0]:>{max_width}.2f}",end=" ")
        print(f"| {legend[i]:>{legend_width-1}}" if i != n-1 else f"|{legend[i]:>{legend_width-1}}",end=" |")
        for j in range(1,m):
            print(f"{a[i][j]:>{max_width}.2f}",end=" |")
            if j == m-1:
                print()
                draw_line()
def legend_simplex(a):
    legend = [] 
    legend.append("Cj")
    for i in range(len(a)-3):
        legend.append(f"S{i+1}")
    legend.append("Zj")
    legend.append("Cj-Zj")
    return legend
def variable_entrante(a):
    n = len(a)
    m = len(a[0])
    v_e = 0
    max = 0
    for j in range(2,m-1):
        if a[n-1][j] >= max:
            max = a[n-1][j]
            v_e = j
    return v_e
def variable_sortante(a,v_e):
    n = len(a)
    m = len(a[0])
    min = a[1][1]
    v_s = 1
    h = 0
    for i in range(1,n-2-h):
        if a[i][v_e] != 0:
            a[i][m-1] = a[i][1]/a[i][v_e] 
            if a[i][m-1] < min:
                min = a[i][m-1]
                v_s = i
        else: h = h+1
  
    if min < 0 :
        print("+-----------------+")
        print("| Pas de Solution |")
        print("+-----------------+")  
        exit()
    return v_s
def calcul_zj(a,min = 0):
    n = len(a)
    m = len(a[0])
    sum = 0
    for i in range(1,m-1):
        for h in range(1,n-2):
            sum += a[h][0] * a[h][i]     
        a[n-2][i] = sum
        sum = 0
    if min == 0 :
        for j in range(2,m-1):
            a[n-1][j] = a[0][j] - a[n-2][j] 
    else:
        for j in range(2,m-1):
            a[n-1][j] =  a[n-2][j] - a[0][j] 
      
    return
def simplexe_normal(a):
    afficher_simplexe(a, "Forme Standard")
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
       
        print(f"* Max = {a[n-1][j_p]}")
        print(f"** Min = {a[i_p][m-1]}")
        print(f"*** Pivot (A[{i_p}][{j_p}]) = {pivot:.2f}")
        afficher_simplexe(a, "Choix Pivot",f"X{i_p}",i_p,j_p)
       
        for j in range(1, m-1):
            a[i_p][j] /= pivot
        for i in range(1, n-2):
            if i != i_p:
                facteur = a[i][j_p]
                for j in range(1, m-1):
                    a[i][j] -= (facteur/pivot) * a[i_p][j]
        calcul_zj(a)
        afficher_simplexe(a, "Apres Elimination",f"X{i_p}",i_p,j_p)
"""
a = [   [0,0,800,300,0,0,0,0],#Cj
        [0,400,2,1,1,0,0,0],#S1,A1
        [0,150,1,0,0,1,0,0],#S2,A2
        [0,200,0,1,0,0,1,0],#S3,A3
        [0,0,0,0,0,0,0,0],#Zj
        [0,0,800,300,0,0,0,0]]#Cj-Zj

#-------CC-------
a = [   [0,0,3,5,0,0,0,0],#Cj
        [0,18,2,1,1,0,0,0],#S1,A1
        [0,42,2,3,0,1,0,0],#S2,A2
        [0,24,3,1,0,0,1,0],#S3,A3
        [0,0,0,0,0,0,0,0],#Zj
        [0,0,3,5,0,0,0,0]]#Cj-Zj

Min Z = 5x + 10y
6x + 2y <= 36
5x + 5y <= 50
x ≥ 0 ;  y ≥ 0 

"""
a = [   [0,0,5,10,0,0,0,0],#Cj
        [0,36,6,2,1,0,0,0],#S1,A1
        [0,50,5,5,0,1,0,0],#S2,A2
        [0,0,0,0,0,0,0,0],#Zj
        [0,0,5,10,0,0,0,0]]#Cj-Zj

legend = legend_simplex(a)

#-----------Main-----------
if __name__ == '__main__':
    with open("simplex.txt", "w") as f:
        with redirect_stdout(f):
            simplexe_normal(a)
