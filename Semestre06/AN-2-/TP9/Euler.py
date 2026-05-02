from Fonction import *

def euler(f, x0, y0, h, n, y_exact=None):
    x = x0
    y = y0
    table = []
    table.append((x, y_exact(x), y) if y_exact else (x, y))
    for k in range(n):
        y = y + h * f(x, y)
        x = round(x + h, 5)
        table.append((x, y_exact(x), y) if y_exact else (x, y))
    afficher_tableau(table)


def euler_rec(f, x0, y0, h, n, y_exact=None, table=None):
    if table is None:
        table = []
        table.append((x0, y_exact(x0), y0) if y_exact else (x0, y0))

    if n == 0:
        afficher_tableau(table)
        return
    y1 = y0 + h * f(x0, y0)
    x1 = round(x0 + h, 5)
    table.append((x1, y_exact(x1), y1) if y_exact else (x1, y1))

    euler_rec(f, x1, y1, h, n - 1, y_exact, table)