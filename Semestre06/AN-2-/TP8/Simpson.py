from Fonction import * 

def simpson(a,b,n):
    h = (b-a)/n
    s1 ,s2 = 0,0
    for i in range(1,n+1):
        x_i = a + (i*h)
        if i : s1 += f_x(x_i)
        x_i_1 = a + ((i+1)*h)
        s2 += f_x((x_i+x_i_1)/2)

    return (h/6) * ( f_x(a) + f_x(b) + 2*s1 + 4*s2)

def simpson_recursive(a, b, n, i=1, s1=0, s2=0):
    h = (b - a) / n    
    if i == n+1:
        return (h /6) * (f_x(a) + f_x(b) + 2 * s1 + 4 * s2)
    
    x_i = a + i * h
    x_i_1 = a + (i + 1) * h
    return simpson_recursive(a, b, n,i + 1,s1 + f_x(x_i),s2 + f_x((x_i + x_i_1) / 2))

def erreur_absolue_simpson(I_ex,a,b,n):
    return round(abs(I_ex - simpson(a,b,n)),4)

def borne_erreur_simpson(a,b,n):
    M_3 = abs(max(f_dddx(a),f_dddx(b)))
    return round((M_3/ 192 * n**3) * (b-a)**4,4)