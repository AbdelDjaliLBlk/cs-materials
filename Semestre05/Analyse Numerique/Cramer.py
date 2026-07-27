def det_rec(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    d = 0
    for j in range(n):
        sub = [row[:j] + row[j+1:] for row in A[1:]]
        d += ((-1)**j) * A[0][j] * det_rec(sub)
    return d
def cramer(A,b):
    n = len(A)
    detA = det_rec(A)
    x = [0.0] * n
    if detA == 0:
        print("+---------Warning:---------+")
        print("|      Determinant = 0     |")
        print("+--------------------------+")
        return x 
    for i in range(n):
        Ai = [row[:] for row in A]
        for k in range(n):
            Ai[k][i] = b[k]
        x[i] = det_rec(Ai) / detA
    return x
def cramer_rec(a,a_i,b,x,i,j,n,det):
    if j == n :
        return 
    if i == 0: 
        a_i = [row[:] for row in a]
    if i == n :
        x[j] = det_rec(a_i)/det
        cramer_rec(a,a_i,b,x,0,j+1,n,det)
    else :
        a_i[i][j] = b[i]
        cramer_rec(a,a_i,b,x,i+1,j,n,det)