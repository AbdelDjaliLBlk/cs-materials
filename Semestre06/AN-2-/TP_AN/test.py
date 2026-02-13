import sympy as sp
from colorama import Fore,Style 

# Declaring The Symbol X and The Points of f(x)
x = sp.Symbol('x')
f = 1/1-x
print(f.subs(x,1))