from Base_functions import *
def max_pivot_total(a,line,col):
    max = abs(a[line][col])
    index_i = line
    index_j = col
    for i in range(line,len(a)):
        for j in range(col, len(a)):
            if abs(a[i][j]) > max : 
                max = a[i][j]
                index_i = i
                index_j = j
    return index_i,index_j
def pivot_total(a,b):
    n = len(a)
    sol = [f"x{i}" for i in range(1,len(a)+1)]
    for k in range(0,n-1):
        i_t,j_t = max_pivot_total(a,k,k)
        if k <= n-2:
           permuter_ligne(a,n,n,k,i_t)
           permuter_colonne(a,n,n,k,j_t)
           sol[k],sol[j_t] = sol[j_t],sol[k] 
           b[k],b[i_t] = b[i_t],b[k]
        pivot = a[k][k]
        if pivot != 0:
            for i in range(k+1,n):
                q = a[i][k]
                a[i][k] = 0
                b[i] = round(b[i]-(q/pivot)*b[k],3)
                for j in range(k+1,n):
                    a[i][j] =round(a[i][j]-a[k][j]*(q/pivot),3)
        print(f"* Itération K={k+1}:")
        afficher_systeme(a,b,sol)
    x = resolution_remontee(a,b)
    print("** Solution :")
    for i in range(0,len(a)):
        print(f"{sol[i]} = {round(x[i],3)}.")    
def pivot_total_rec(a,b,n,i,j,k,factor,x):
    if k == n-1:
        print("** Solution:")
        sol = resolution_remontee(a,b)
        if sol:
            print_res_rec(sol,x,0,n)
        return
    if i == k and j == k:
        index_i , index_j = max_pivot_total(a,k,k)
        permuter_ligne(a,n,n,i,index_i)
        permuter_colonne(a,n,n,j,index_j)
        b[i],b[index_i] = b[index_i],b[i]
        x[i],x[index_i] = x[index_i],x[i]
        pivot_total_rec(a,b,n,k+1,k,k,0,x)
    elif i == n :
        print(f"* Itération K={k+1}:")
        afficher_systeme(a,b,x,None)
        pivot_total_rec(a,b,n,k+1,k+1,k+1,0,x)
    elif j == k:
        factor = a[i][k] / a[k][k]
        b[i] = b[i] - (factor*b[k])
        a[i][k] = 0
        pivot_total_rec(a,b,n,i,k+1,k,factor,x)     
    elif j == n :
        pivot_total_rec(a,b,n,i+1,k,k,0,x)
    else:
        a[i][j] -= a[k][j]*factor
        pivot_total_rec(a,b,n,i,j+1,k,factor,x)
