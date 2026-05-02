from Fonction import *

def point_milieu(f, x0, y0, h, n, y_exact=None):
    x = x0
    y = y0
    table = []
    table.append((x, y_exact(x), y) if y_exact else (x, y))
    for k in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        y = y + k2
        x = round(x + h, 10)
        table.append((x, y_exact(x), y) if y_exact else (x, y))
    afficher_tableau(table)


def point_milieu_rec(f, x0, y0, h, n, y_exact=None, table=None):
    if table is None:
        table = []
        table.append((x0, y_exact(x0), y0) if y_exact else (x0, y0))
    if n == 0:
        afficher_tableau(table)
        return
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + h/2, y0 + k1/2)
    y1 = y0 + k2
    x1 = round(x0 + h, 10)
    table.append((x1, y_exact(x1), y1) if y_exact else (x1, y1))
    point_milieu_rec(f, x1, y1, h, n - 1, y_exact, table)

