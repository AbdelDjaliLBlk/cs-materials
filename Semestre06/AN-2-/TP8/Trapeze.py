from Fonction import * 

def trapeze(a,b,n):
    h = (b-a)/n
    s = 0
    for i in range(1,n):
        x_i = a + (i*h)
        s += f_x(x_i)
    return h * ((f_x(a)+f_x(b))/2 + s)

def trapeze_recursive(a,b,n,i=1,s=0):
    if i == n:
        return ((b-a)/n) * ((f_x(a)+f_x(b))/2 + s) 
    x_i = a + (i * ((b-a)/n) )
    trapeze_recursive(a,b,n,i+1,s + f_x(x_i))

def erreur_absolue_trapeze(I_ex,a,b,n):
    return round(abs(I_ex - trapeze(a,b,n)),4)

def borne_erreur_trapeze(a,b,n):
    M_2 = abs(max(f_dx(a),f_dx(b)))
    return round((M_2/ 12 * n**2) * (b-a)**3,4)