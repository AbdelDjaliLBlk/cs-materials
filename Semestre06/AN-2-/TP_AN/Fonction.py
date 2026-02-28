import math

def f_x(x):
    return x**3 + 4*x**2 - 10
def df_x(x):
    return 3*x**2 + 4*x
def g_x(x):    
    return math.sqrt((10 - x**3)/4)
def dg_x(x):
    return x