import math
import sympy as sp
x = sp.Symbol('x')

# f(x) , g(x)
f = x**3 + 4*x**2 - 10
g = 10 /(x**2+4*x)

def f_x(y):
    return f.subs(x,y) 
def df_x(y):
    return sp.diff(f,x).subs(x,y)
def g_x(y):    
    return g.subs(x,y)


print(g_x(4))