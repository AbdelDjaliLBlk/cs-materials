def racine_point_fixe(a,b,x0,eps):
    if x0 > b or x0 < a:
        print(f"{x0} not in [{a},{b}].")
        return
    # ---Functions---
    def draw_line():
        for _ in range(m):
            print("+",end="")
            for __ in range(max_width+1):
                print("-",end="")
        print("+")
    #-----Affichage-----
    x_i = x0
    x_n = g_x(x0)
    k = 0
    t = [k,x_i,x_n,abs(x_n-x_i)] 
    x_char = ['N','X(n)','X(n+1)','X(n+1)-X(n)']
    m = len(x_char)
    max_width = max(max((len(f"{t[i]:.4f}")) for i in range(m)),12)
    # Etat Initial
    draw_line()
    for i in range(m):    
        print(f"|{x_char[i]:>{max_width}} ",end="")
    print("|")
    draw_line()
    # Procedure Point Fixe
    while (abs(x_n - x_i) > eps):
        x_i = x_n 
        x_n = g_x(x_n)
        t = [k,x_i,x_n,abs(x_n-x_i)]
        print(f"|{t[0]:>{max_width}}",end=" ")   
        for j in range(1,m):
            print(f"|{t[j]:>{max_width}.4f} ",end="")    
        print("|")
        draw_line()
        k = k+1
        t = []
