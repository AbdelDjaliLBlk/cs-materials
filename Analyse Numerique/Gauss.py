from Base_functions import * 
def pivot_gauss(a,b):
    n = len(a)
    for k in range(0,n-1):
        pivot = a[k][k]
        if pivot != 0:
            for i in range(k+1,n):
                q = a[i][k]
                a[i][k] = 0
                b[i] = round(b[i]-(q/pivot)*b[k],3)
                for j in range(k+1,n):
                    a[i][j] =round(a[i][j]-a[k][j]*(q/pivot),3)
            
        else:
            print("+-----Warning:-----+")
            print("|    Pivot nul !!  |")
            print("+------------------+")
            return
        print(f"* Itération K={k+1}:")
        afficher_systeme(a,b)
    print("** Résolution donne:\n",resolution_remontee(a,b))
def pivot_gauss_rec(a,b,i,j,k,factor,size):
    if k == size-1:
        print("** Solution:")
        sol = resolution_remontee(a,b)
        if sol:
            print_res_rec(sol,None,0,size)
        return
    
    if i == size:
        print(f"* Itération K={k+1}:")
        afficher_systeme(a,b)
        pivot_gauss_rec(a, b, k+2, k+1, k+1,0,size)    
    elif j==k:
        if a[k][k] == 0:
            print("+-----Warning:-----+")
            print("|    Pivot nul !!  |")
            print("+------------------+")
            return
        factor = a[i][k] / a[k][k]
        b[i] = b[i] - (factor * b[k])
        a[i][k] = 0
        pivot_gauss_rec(a,b,i,k+1,k,factor,size)
    elif j == size:
        pivot_gauss_rec(a, b, i+1, k, k, factor ,size)
    else:
        a[i][j] -= factor* a[k][j]
        pivot_gauss_rec(a,b,i,j+1,k,factor,size)