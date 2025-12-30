from Base_functions import * 
def division_rec(a,I,i,j,n):
    if i >= n :
        return
    elif j >= n :
        division_rec(a,I,i+1,0,n)
    else:
        I[i][j] /= a[i][i]
        a[i][j] /= a[i][i]
        division_rec(a,I,i,j+1,n)
def gauss_jordan(a,b):
    n = len(a)
    I = matrice_identite(n)
    for k in range(0,n):
        pivot = a[k][k]
        if pivot != 0:
            for i in range(0,n):
                if i != k:
                    q = a[i][k]
                    a[i][k] = 0
                    b[i] = round(b[i]-(q/pivot)*b[k],3)
                    for j in range(k+1,n):
                        a[i][j] =round(a[i][j]-a[k][j]*(q/pivot),3)
                        I[i][j] =round(I[i][j]-a[k][j]*(q/pivot),3) 
            print(f"* Itération K={k+1}:")
            afficher_systeme(a,b,None,I)
        else:
            print("+-----Warning:----+")
            print("|    Pivot Nul!   |")
            print("+-----------------+")
            return
    print("** Solution:\nx =",resolution_remontee(a,b))
    for i in range(n):
      for j in range(n):
          I[i][j] /= a[i][i]
          a[i][j] /= a[i][i]
    print(f"*** Division:")
    afficher_systeme(a,b,None,I)
    afficher_matrice(I,n,n,"*** Inverse de A")
def gauss_jordan_rec(a,b,I,n,i,j,k,factor):
    if k == n:
        print("\n** Matrice Reduite :")
        afficher_systeme(a,b,None, I)
        print(f"\n*** Solution Recursive: {resolution_remontee(a,b)}")
        return 
    if i >= n:
        print(f"* Itération K={k+1}:")
        afficher_systeme(a,b,None,I)
        gauss_jordan_rec(a,b,I,n,0,0,k+1,0)
    elif j == n :
        gauss_jordan_rec(a,b,I,n,i+1,0,k,factor)
    elif i == k :
        gauss_jordan_rec(a,b,I,n,i+1,0,k,factor)
    else:
        if j == 0 : 
            factor = a[i][k]/a[k][k]
            b[i] = b[i] - (b[k] * factor)
        a[i][j] = a[i][j] - a[k][j] * factor
        I[i][j] = I[i][j] - a[k][j] * factor
        a[i][k] = 0
        gauss_jordan_rec(a,b,I,n,i,j+1,k,factor)
