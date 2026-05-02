from Fonction import *

def euler_mod(f, x0, y0, h, n, y_exact=None):
    x = x0
    y = y0
    table = []
    table.append((x, y_exact(x), y) if y_exact else (x, y))
    for k in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y = y + (h / 2) * (k1 + k2)
        x = round(x + h, 10)
        table.append((x, y_exact(x), y) if y_exact else (x, y))
    afficher_tableau(table)


def euler_mod_rec(f, x0, y0, h, n, y_exact=None, table=None):
    if table is None:
        table = []
        table.append((x0, y_exact(x0), y0) if y_exact else (x0, y0))
    if n == 0:
        afficher_tableau(table)
        return
    k1 = f(x0, y0)
    k2 = f(x0 + h, y0 + h * k1)
    y1 = y0 + (h / 2) * (k1 + k2)
    x1 = round(x0 + h, 10)
    table.append((x1, y_exact(x1), y1) if y_exact else (x1, y1))
    euler_mod_rec(f, x1, y1, h, n - 1, y_exact, table)
