from Fonction import *

def taylor(f, dfdx, dfdy, x0, y0, h, n, y_exact=None):
    x = x0
    y = y0
    table = []
    table.append((x, y_exact(x), y) if y_exact else (x, y))
    for k in range(n):
        f_val = f(x, y)
        dfdx_val = dfdx(x, y)
        dfdy_val = dfdy(x, y)
        y = y + h * f_val + (h**2 / 2) * (dfdx_val + dfdy_val * f_val)
        x = round(x + h, 10)
        table.append((x, y_exact(x), y) if y_exact else (x, y))
    afficher_tableau(table)


def taylor_rec(f, dfdx, dfdy, x0, y0, h, n, y_exact=None, table=None):
    if table is None:
        table = []
        table.append((x0, y_exact(x0), y0) if y_exact else (x0, y0))
    if n == 0:
        afficher_tableau(table)
        return
    f_val = f(x0, y0)
    dfdx_val = dfdx(x0, y0)
    dfdy_val = dfdy(x0, y0)
    y1 = y0 + h * f_val + (h**2 / 2) * (dfdx_val + dfdy_val * f_val)
    x1 = round(x0 + h, 10)
    table.append((x1, y_exact(x1), y1) if y_exact else (x1, y1))
    taylor_rec(f, dfdx, dfdy, x1, y1, h, n - 1, y_exact, table)
