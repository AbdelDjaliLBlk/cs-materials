# ==================
#      Lagrange
# ==================
def interpolation_lagrange(point,x,n):
    L = 0
    x_i = []
    y_i = []
    for xi,yi in point:
        x_i.append(xi)
        y_i.append(yi)
    for i in range(n):
        l_i = 1
        for j in range(n):
            if j != i:
                l_i *= (x-x_i[j])/(x_i[i] - x_i[j])
        L += l_i * y_i[i]
    return L

