def interpolation_newton(points, x):
    X = [] ; Y = []
    for x_i,y_i in points:
        X.append(x_i)
        Y.append(y_i)
    n = len(points)
    #-----Affichage-----
    x_char = ['X','F(X)'] + [f"DD**{k}" for k in range(1,n)]
    m = len(x_char)
    max_width = max(max([len(f"{X[i]:.4f}") for i in range(n)]),12)

    def draw_line():
        for _ in range(m):
            print("+",end="")
            for __ in range(max_width+1):
                print("-",end="")
        print("+")

    # Differences Divisees
    DD = [[0]*n for _ in range(n)]
    for i in range(n):
        DD[i][0] = Y[i]
    for j in range(1,n):
        for i in range(n-j):
            DD[i][j] = (DD[i+1][j-1] - DD[i][j-1]) / (X[i+j] - X[i])

    # Etat Initial
    draw_line()
    for i in range(m):
        print(f"|{x_char[i]:>{max_width}} ",end="")
    print("|")
    draw_line()
    for i in range(n):
        print(f"|{X[i]:>{max_width}.4f} ",end="")
        print(f"|{DD[i][0]:>{max_width}.4f} ",end="")
        for j in range(1,n):
            if i+j < n:
                print(f"|{DD[i][j]:>{max_width}.4f} ",end="")
            else:
                print(f"|{'':>{max_width}} ",end="")
        print("|")
        draw_line()

    # Procedure Newton
    N = DD[0][0]
    p = 1
    for k in range(1,n):
        p *= (x - X[k-1])
        N += DD[0][k] * p
    return N
def interpolation_newton_rec(points, x):
    X = [x_i for x_i, _ in points]
    Y = [y_i for _, y_i in points]
    n = len(points)

    # -----Affichage-----
    x_char = ['X', 'F(X)'] + [f"DD**{k}" for k in range(1, n)]
    m = len(x_char)
    max_width = max(max([len(f"{X[i]:.4f}") for i in range(n)]), 12)

    def draw_line():
        for _ in range(m):
            print("+", end="")
            for __ in range(max_width + 1):
                print("-", end="")
        print("+")

    # Differences Divisees (Recursive)
    def DD(i, j):
        if j == 0:
            return Y[i]
        return (DD(i + 1, j - 1) - DD(i, j - 1)) / (X[i + j] - X[i])

    # Etat Initial
    draw_line()
    for i in range(m):
        print(f"|{x_char[i]:>{max_width}} ", end="")
    print("|")
    draw_line()
    for i in range(n):
        print(f"|{X[i]:>{max_width}.4f} ", end="")
        print(f"|{DD(i, 0):>{max_width}.4f} ", end="")
        for j in range(1, n):
            if i + j < n:
                print(f"|{DD(i, j):>{max_width}.4f} ", end="")
            else:
                print(f"|{'':>{max_width}} ", end="")
        print("|")
        draw_line()

    # Procedure Newton (Recursive)
    def newton(k, p):
        if k == n:
            return 0
        return DD(0, k) * p + newton(k + 1, p * (x - X[k]))

    return DD(0, 0) + newton(1, x - X[0])