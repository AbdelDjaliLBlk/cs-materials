from Fonction import * 

def rectangle_droite(a,b,n):
    h = (b-a)/n
    s = 0
    for i in range(1,n+1):
        x_i = a + (i*h)
        s += f_x(x_i)
    return h * s 

def rectangle_milieu(a,b,n):
    h = (b-a)/n
    s = 0
    for i in range(n-2):
        # On Prend les Milieus
        x_i = a + (i*h)
        x_i_1 = a + ((i+1)* h)
        s += f_x(round((x_i+ x_i_1)/2,3))
    return h *s

def rectangle_gauche(a,b,n):
    h = (b-a)/n
    s = 0
    for i in range(n):
        x_i = a + (i*h)
        s += f_x(x_i)
    return h * s

def rectangle_droite_recursive(a, b, n, i=1, s=0):
    h = (b - a) / n
    if i == n+1:
        return h * s
    x_i = a + (i * h)
    return rectangle_droite_recursive(a, b, n, i + 1, s + f_x(x_i))


def rectangle_milieu_recursive(a, b, n, i=0, s=0):
    h = (b - a) / n
    if i == n - 2:
        return h * s
    x_i   = a + (i * h)
    x_i_1 = a + ((i + 1) * h)
    mid   = round((x_i + x_i_1)/2,3)
    return rectangle_milieu_recursive(a, b, n, i + 1, s + f_x(mid))


def rectangle_gauche_recursive(a, b, n, i=0, s=0):
    h = (b - a) / n
    if i == n :
        return h * s
    x_i = a + (i * h)
    return rectangle_gauche_recursive(a, b, n, i + 1, s + f_x(x_i)) 

def erreur_absolue(I_ex,a,b,n):
    return round(abs(I_ex - rectangle_gauche(a,b,n)),4)

def borne_erreur(a,b,n):
    M_1 = abs(max(f_dx(a),f_dx(b)))
    return round((M_1/ 2*n) * (b-a)**2,4)
