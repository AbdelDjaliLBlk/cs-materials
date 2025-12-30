from Base_functions import *
def condition_lu(a,n):
    for k in range(n+1):
        sub = [row[:k] for row in a[:k]]
        s = len(sub)
        if determinant(sub,s,s) == 0:
            return True
    return False
def decomposition_lu(a,b):
    n = len(a)
    l = matrice_identite(n)
    for i in range(n) : l[i][i] = 1
    
    #------------------Décomposition-------------------
    print(f"------------1- Décomposition:------------")
    print("*A = L * U")
    afficher_matrice(a,n,n,"-->La Matrice U0")
    afficher_matrice(l,n,n,"-->La Matrice L0")
    print()
    for k in range(n+1): 
        sub = [row[:k] for row in a[:k]]
        s = len(sub)
        if determinant(sub,s,s) == 0:
            print(f"------------Warning:------------")
            print("* Décomposition LU n'existe pas.")
            return

    for k in range(n-1):
        pivot = a[k][k]
        print(f"***Itération K={k+1}:")
        print(f" ** pivot = {pivot}.")
        for i in range(k+1,n):
            q = a[i][k]
            l[i][k] = q/pivot
            a[i][k] = 0
            for j in range(k+1,n):
                a[i][j] =round(a[i][j]-a[k][j]*(q/pivot),3)
        
        afficher_matrice(a,n,n,f"  * La Matrice U{k+1}")
        afficher_matrice(l,n,n,f"  * La Matrice L{k+1}")
        print()

        
    u = [x for x in a]
    
    afficher_matrice(u,n,n,f"*La Matrice U")
    afficher_matrice(l,n,n,f"\n*La Matrice L")
    
    #------------------Résoudre Ly = b par descente------------------
    print("-------------Résoudre Ly = b par descente---------------")
    y_char = [f"y{i}" for i in range(1,n+1)]
    y = resolution_descente(l,b)
    print("* Système réduit :")
    afficher_systeme(l,b,y_char)
    print("** Résultat donne:")
    for i in range(n):
        print(f"y{i+1} = {y[i]}.")
    #------------------Résoudre Ux = y par remontée------------------
    print("-------------Résoudre Ux = y par remontée---------------")
    x_char = [f"x{i}" for i in range(1,n+1)]
    x = resolution_remontee(u,y)
    print("* Système réduit :")
    afficher_systeme(u,y,x_char)
    print("** Résultat donne:")
    #------------------Solution------------------
    for i in range(n):
        print(f"x{i+1} = {x[i]}.")   
    return
def decomposition_lu_rec(a,b,l,n,i,j,k,factor):
    if k >= n-1 :
        afficher_matrice(a,n,n,f"*La Matrice U")
        afficher_matrice(l,n,n,f"\n*La Matrice L")
        #------------------Résoudre Ly = b par descente------------------
        print("-------------Résoudre Ly = b par descente---------------")
        y_char = [f"y{i}" for i in range(1,n+1)]
        y = resolution_descente(l,b)
        print("* Système réduit :")
        afficher_systeme(l,b,y_char)
        print("** Résultat Recursif donne:")
        print_res_rec(y,y_char,0,n)
        #------------------Résoudre Ux = y par remontée------------------
        print("-------------Résoudre Ux = y par remontée---------------")
        x_char = [f"x{i}" for i in range(1,n+1)]
        x = resolution_remontee(a,y)
        print("* Système réduit :")
        afficher_systeme(a,y,x_char)
        print("** Résultat Recursif donne:")
        #------------------Solution------------------
        print_res_rec(x,x_char,0,n)
        return
    if i == 1 and j == 0:
        print("* Le Systeme est: ")
        afficher_systeme(a,b)
        print(f"------------1- Décomposition Recursive:------------")
        print("* A = L * U")
        afficher_matrice(a,n,n,"-->La Matrice U0")
        afficher_matrice(l,n,n,"-->La Matrice L0")
        print()
    if i == n :
        print(f"***Itération K={k+1}:")
        print(f" ** pivot = {a[k][k]}.")
        afficher_matrice(a,n,n,f"  * La Matrice U{k+1}")
        afficher_matrice(l,n,n,f"  * La Matrice L{k+1}")
        print()
        decomposition_lu_rec(a,b,l,n,k+1,k+1,k+1,0)
    elif j == n :
        if i != k:
            l[i][k] = factor
        decomposition_lu_rec(a,b,l,n,i+1,0,k,factor)   
    else:
        if j == 0 :
            factor = a[i][k] / a[k][k]
        a[i][j] = a[i][j] - (a[k][j] * factor)
        decomposition_lu_rec(a,b,l,n,i,j+1,k,factor)