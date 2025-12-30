from Base_functions import *
def pivot_partiel(a,b):
    n = len(a)
    for k in range(0,n-1):
        max_k = max_pivot(a,k)
        if k <= n-2:
            permuter_ligne(a,n,n,k,max_k)
        tmp = b[k]
        b[k] = b[max_k]
        b[max_k] = tmp
        pivot = a[k][k]
        for i in range(k+1,n):
            q = a[i][k]
            a[i][k] = 0
            b[i] = round(b[i]-(q/pivot)*b[k],3)
            for j in range(k+1,n):
                a[i][j] =round(a[i][j]-a[k][j]*(q/pivot),3)
        print(f"------------Itération K={k+1}:------------")
        afficher_systeme(a,b)
    return   
def pivot_partiel_rec(a,b,n,i,j,k,factor):
    if k == n-1:
        print("** Solution:")
        sol = resolution_remontee(a,b)
        if sol:
            print_res_rec(sol,None,0,n)
        return
    if i == k :
        max_row = max_pivot(a,k)
        permuter_ligne(a,n,n,k,max_row)
        b[k], b[max_row] = b[max_row], b[k]
        if a[k][k]== 0:
            print("Pivot nul !!")
            return            
        pivot_partiel_rec(a,b,n,k+1,k,k,0)
    elif i == n:
        print(f"* Itération K = {k+1}")
        afficher_systeme(a,b)    
        pivot_partiel_rec(a,b,n,k+1,k+1,k+1,0)
    elif j == k:
        factor = a[i][k] / a[k][k]
        b[i] -=  factor * b[k] 
        a[i][k] = 0
        pivot_partiel_rec(a,b,n,i,k+1,k,factor)     
    elif j == n :
        pivot_partiel_rec(a,b,n,i+1,k,k,0)
    else:
        a[i][j] -= a[k][j]* factor
        pivot_partiel_rec(a,b,n,i,j+1,k,factor)