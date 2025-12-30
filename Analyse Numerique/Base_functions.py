def lire_matrice(t,n,m):
    for i in range (0,n):
        for j in range(0,m):
           print(f"* A[{i}][{j}]= ",end = "")
           t[i][j] = int(input())
def afficher_matrice(a,n,m,nom = None):
    n = len(a)
    max_width = 0
    if nom :
        print(f"{nom}:")
    for i in range(n):
        for j in range(n):
            max_width = max(max_width, len(f"{a[i][j]:.2f}"))
    for i in range(n):
        print("[ ", end="")
        for j in range(n):
            print(f"{a[i][j]:>{max_width}.2f}", end=" ")
            if j < n - 1:
                print("", end="")
        print("]  ")
def afficher_systeme(a, b, x=None, I=None):
    n = len(a)
    length = [0] * n
    for j in range(n):
        length[j] = max(len(f"{a[i][j]:.2f}") for i in range(n))

    b_width = max(len(f"{b[i]:.2f}") for i in range(n))
    x_width = max(len(str(x[i])) for i in range(n)) if x is not None else 0
    I_width = [0] * n
    if I is not None:
        for j in range(n):
            I_width[j] = max(len(f"{I[i][j]:.2f}") for i in range(n))

    for i in range(n):
        print("[ ", end="")
        for j in range(n):
            print(f"{a[i][j]:>{length[j]}.2f}", end=" " if j < n-1 else "")
        print(" ]  ", end="")
        
        if x is not None:
            print("[", end="")
            print(f"{x[i]:>{x_width}}", end="")
            print("]  ", end="")

        print("[", end="")
        print(f"{b[i]:>{b_width}.2f}", end="")
        print("]  ", end="")

        if I is not None:
            print("[", end="")
            for j in range(n):
                print(f"{I[i][j]:>{I_width[j]}.2f}", end=" " if j < n-1 else "")
            print("]", end="")
        print()
def matrice_identite(n):
    if n < 2 :
        print("Error , order < 2 !")
        return   
    I = [[0 for j in range(0,n)] for i in range(0,n)]
    for i in range(0,n):
        I[i][i] = 1
    return I
def somme_matrice(t,n,m,v,a,b):
    if n !=a and b!= m:
        print("Error,Can't sum")
        return
    print(" A + B ")
    for i in range(0,n):
        print("[",end="")
        for j in range(0,m):
            print(t[i][j] + v[i][j],end=" ")
        print("]")
def mult_matrice(t,n,m,v,a,b,msg=None):
    if m != a :
        print("Error,Can't Multiply!")
        return
    C = [[0 for j in range(0,b)] for i in range(0,n)]
    for i in range(0,n):
        for j in range(0,b):
            for h in range(0,a):
               C[i][j] += t[i][h] * v[h][j]    
    afficher_matrice(C,n,b,msg)
def matrice_trans(t,n,m):
    At = [[0 for j in range (0,n)] for i in range(0,m)]
    for i in range(0,m):
        for j in range(0,n):
            At[i][j] = t[j][i]
    afficher_matrice(At,m,n)
def tri_sup(t,n,m):
    if n != m:
        return False
    for i in range (1,n):
        for j in range (0,i):
             if t[i][j] != 0:
                 return False
    return True
def tri_inf(t,n,m):
    if n != m:
        return False
    for i in range (0,n-1):
        for j in range (i+1,n):
             if t[i][j] != 0:
                 return False
    return True
def matrice_diagonale(t,n,m):
    if tri_inf(t,n,m) and tri_sup(t,n,m):
        return True
    #Or checking for i!=j t[i][j] == 0
    return False
def matrice_sym(t,n,m):
    if n!=m :
        return False
    for i in range(0,n):
        for j in range(0,n):
            if t[i][j] != t[j][i]:
                return False
    return True
def determinant(t,n,m):
    det = 1.0
    if tri_sup(t, n, m) or tri_inf(t,n,m):
        for i in range(n):
            det *= t[i][i]
        return det
    elif n==1 : 
        return t[0][0]
    elif t == matrice_identite(n):
        return 1

    elif n == 2 :
        return t[0][0]*t[1][1] - t[0][1]*t[1][0]

    submat = [row[:] for row in t]
    for i in range(n):
        x = i
        for j in range(i+1,n):
            if abs(submat[j][i]) > abs(submat[x][i]):
                x = j
        if x != i:
            submat[i] , submat[x] = submat[x] , submat[i]
            det *=-1

        for j in range(i+1,n):
            y = submat[j][i] / submat[i][i]
            for h in range(i+1,n):
                submat[j][h] -= y * submat[i][h]
            submat[j][i] = 0
        det *= submat [i][i]
    return det
def determinant_rec(t):
    n = len(t)
    if n == 2 :
        return t[0][0] * t[1][1] - t[0][1] * t[1][0]

    def cofactor_sum(i=0):
        if i == n:
            return 0
        minor = [row[:i] + row[i+1:] for row in t[1:]]
        return ((-1)**i * t[0][i] * determinant_rec(minor)) + cofactor_sum(i+1)

    return cofactor_sum()
def permuter_ligne(t,n,m,l1,l2):
    if l1 >= n or l2 >=n :
        print("Out of index!")
    for j in range(0,m):
        tmp = t[l1][j]
        t[l1][j] = t[l2][j]
        t[l2][j] = tmp
    return t
def permuter_colonne(t,n,m,l1,l2):
    if l1 >= m or l2 >=m :
        print("Out of index!")
    for i in range(0,n):
        tmp = t[i][l1]
        t[i][l1] = t[i][l2]
        t[i][l2] = tmp
    return t
def sum_rec(a,x,i,j):
    if j >= len(a):
        return 0
    return a[i][j] * x[j] + sum_rec(a,x,i,j+1)
def resolution_remontee(a,b):
    n = len(a)
    if not tri_sup(a,n,n):
        print("A n'est pas triangulaire supèrieur!")
        return
    x = [0] * n
    sum = 0
    x[n-1] = round(b[n-1]/a[n-1][n-1],3)
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            sum += a[i][j] * x[j]
        x[i] = round((b[i] - sum)/a[i][i],3)
        sum = 0.0
    return x
def resolution_descente(a,b):
    n = len(a)
    if not tri_inf(a,n,n):
        print("A n'est pas triangulaire infèrieur!")
        return
    x = [0] * n
    sum = 0
    x[0] = round(b[0]/a[0][0],3)
    for i in range(1,n):
        for j in range(0,n):
            sum += a[i][j] * x[j]
        x[i] = round((b[i] - sum)/a[i][i],3)
        sum = 0.0
    return x
def resolution_remontee_rec(a,b,x,i):
    if i < 0 :
        return 0
    s = sum_rec(a,x,i,i+1)
    x[i] = round((b[i] - s)/a[i][i],3)
    resolution_remontee_rec(a,b,x,i-1)
def resolution_descente_rec(a,b,x,i):
    if i >= len(a) :
        return 0
    s = sum_rec(a,x,i,0)
    x[i] = round((b[i] - s)/a[i][i],3)   
def max_pivot(a,k):
    max = abs(a[k][k])
    index = k
    for i in range(k,len(a)):
        if abs(a[i][k]) > max : 
            max = a[i][k]
            index = i
    return index
def print_res_rec(x,x_s,i,n):
    if i == n:
        return
    if x_s is None:
        x_s = [f"x{i+1}" for i in range(n)]
    print(f" {x_s[i]} = {x[i]:.4f}")
    print_res_rec(x,x_s,i+1,n)
def diagonale_dominante(a):
    n = len(a)
    for i in range(n):
        diag = abs(a[i][i])
        others = sum(abs(a[i][j]) for j in range(n) if j != i)
        if diag < others:
            return False
    return True
