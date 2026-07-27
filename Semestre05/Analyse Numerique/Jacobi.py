from Base_functions import *
def jacobi(a,b,iteration):
    n = len(a)
    if not diagonale_dominante(a):
        print("+------------Warning:------------+")
        print("|     Diagonale non_dominante    |")
        print("+--------------------------------+")
        return
    x = [0.0] * n   
    x_new = [0.0] * n
    for k in range(iteration):
        print(f"* Itération K={k+1}:")
        for i in range(n):
            s = sum(a[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / a[i][i]
        x = x_new[:]   
        for i in range(n):
            print(f"x{i+1} = {round(x[i],4)}")
    return     
def jacobi_rec(a,b,n,x,x_new,i,j,k,c):
    if not diagonale_dominante(a):
        print("+------------Warning:------------+")
        print("|     Diagonale non_dominante    |")
        print("+--------------------------------+")
        return
    if k <= 0:
        print("** FIN")
        return
    if i == n :
        print(f"* Iteration K = {c}")
        print_res_rec(x_new,None,0,n)
        x = x_new[:]
        jacobi_rec(a,b,n,x,x_new,0,0,k-1,c+1)
    elif j == n :
        x_new[i] = x_new[i] + b[i]/a[i][i] 
        jacobi_rec(a,b,n,x,x_new,i+1,0,k,c)
    else :
        x_new[i] = x_new[i] - (a[i][j]* x[j])/a[i][i] 
        jacobi_rec(a,b,n,x,x_new,i,j+1,k,c)
def jacobi_precision_rec(x,x_new,i,n):
    if i == n :
        return 0
    return max(abs(x_new[i] - x[i]),jacobi_precision_rec(x,x_new,i+1,n))
def jacobi_epsilon_rec(a,b,n,x,x_new,i,j,epsilon,precision):
    if not diagonale_dominante(a):
        print("+------------Warning:------------+")
        print("|     Diagonale non_dominante    |")
        print("+--------------------------------+")
        return
    if precision <= epsilon:
        return
    if i == n :
        p = jacobi_precision_rec(x,x_new,0,n)
        print(f"* Precision = {round(p,len(f"{epsilon}"))}",)  
        x = x_new[:]
        print_res_rec(x_new,None,0,n)
        jacobi_epsilon_rec(a,b,n,x,x_new,0,0,epsilon,p)
    elif j == n :
        x_new[i] = x_new[i] + b[i]/a[i][i] 
        jacobi_epsilon_rec(a,b,n,x,x_new,i+1,0,epsilon,precision)
    else :
        x_new[i] = x_new[i] - (a[i][j]* x[j])/a[i][i] 
        jacobi_epsilon_rec(a,b,n,x,x_new,i,j+1,epsilon,precision)
def jacobi_epsilon(a,b,epsilon):
    n = len(a)
    if not diagonale_dominante(a):
        print("+------------Warning:------------+")
        print("|     Diagonale non_dominante    |")
        print("+--------------------------------+")
        return
    x = [0.0] * n   
    x_new = [0.0] * n
    while True:
        for i in range(n):
            s = sum(a[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / a[i][i]
        precision = max(abs(x_new[i] - x[i]) for i in range(n))
        if precision <= epsilon: break
        print(f"--->Precision = {round(precision,len(f"{epsilon}"))}.")  
        x = x_new[:]   
        for i in range(n):
            print(f"x{i+1} = {round(x[i],4)}")