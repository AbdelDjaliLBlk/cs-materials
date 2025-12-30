from Base_functions import *
from Jacobi import jacobi_precision_rec
def gauss_seidel(a,b,iteration):
    n = len(a)
    if not diagonale_dominante(a):
        print("+------------Warning:------------+")
        print("|     Diagonale non_dominante    |")
        print("+--------------------------------+")
        return
    
    x = [0.0] * n   
    for k in range(iteration):
        print(f"* Itération K={k+1}:")
        for i in range(n):
            s = sum(a[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / a[i][i]

        for i in range(n):
            print(f"x{i+1} = {round(x[i],4)}")
def gauss_seidel_epsilon(a,b,epsilon):
    n = len(a)
    if not diagonale_dominante(a):
        print("+------------Warning:------------+")
        print("|     Diagonale non_dominante    |")
        print("+--------------------------------+")
        return
    x = [0.0] * n
    x_i = [0.0] * n   
    while True :
        for i in range(n):
            s = sum(a[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / a[i][i]
        precision = max(abs(x[i] - x_i[i])for i in range(n))
        if precision < epsilon:
            break
        else :
            length = len(f"{epsilon}")
            print(f"---> Precision = {round(precision,length)}.")     
        x_i = x[:]
        for i in range(n):
            print(f"x{i+1} = {round(x[i],4)}")
def gauss_seidel_rec(a,b,n,x,i,j,k,c):
    if not diagonale_dominante(a):
        print("+------------Warning:------------+")
        print("|     Diagonale non_dominante    |")
        print("+--------------------------------+")
        return
    if k <= 0:
        return
    if i == n :
        print(f"* Iteration K = {c+1}")
        print_res_rec(x,None,0,n)
        gauss_seidel_rec(a,b,n,x,0,0,k-1,c+1)
    elif j == n :
        x[i] = x[i] + (b[i]/a[i][i])
        gauss_seidel_rec(a,b,n,x,i+1,0,k,c)
    else :    
        x[i] = x[i] - ((a[i][j]* x[j])/a[i][i])
        gauss_seidel_rec(a,b,n,x,i,j+1,k,c)
def gauss_seidel_epsilon_rec(a,b,n,x,x_i,i,j,epsilon,precision):
    if precision <= epsilon:
        print("** Convergence Atteinte.")
        return
    if i == n :
        precision = jacobi_precision_rec(x,x_i,0,n)
        print(f"* Precision = {precision:.{len(str(epsilon).split('.')[-1])}f}")
        x_i = x[:]  
        print_res_rec(x,None,0,n)
        gauss_seidel_epsilon_rec(a,b,n,[0]*n,x,0,0,epsilon,precision)
    elif j == n :
        x[i] +=  b[i] / a[i][i]
        gauss_seidel_epsilon_rec(a,b,n,x,x_i,i+1,0,epsilon,precision)
    else :
        if i != j:
            x[i] -= ( a[i][j] * x[j] ) / a[i][i] 
        gauss_seidel_epsilon_rec(a,b,n,x,x_i,i,j+1,epsilon,precision)
