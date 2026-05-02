from Fonction import *

def RK4(f, x0, y0, h, n, y_exact=None):
    x = x0
    y = y0
    table = []
    table.append((x, y_exact(x), y) if y_exact else (x, y))
    for k in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        x = round(x + h, 10)
        table.append((x, y_exact(x), y) if y_exact else (x, y))
    afficher_tableau(table)


def RK4_rec(f, x0, y0, h, n, y_exact=None, table=None):
    if table is None:
        table = []
        table.append((x0, y_exact(x0), y0) if y_exact else (x0, y0))
    if n == 0:
        afficher_tableau(table)
        return
    K1 = h * f(x0, y0)
    K2 = h * f(x0 + h/2, y0 + K1/2)
    K3 = h * f(x0 + h/2, y0 + K2/2)
    K4 = h * f(x0 + h, y0 + K3)
    
    y1 = y0 + (1/6) * (K1 + 2*(K2 + K3) + K4)

    x1 = round(x0 + h, 10)
    
    table.append((x1, y_exact(x1), y1) if y_exact else (x1, y1))
    RK4_rec(f, x1, y1, h, n - 1, y_exact, table)
