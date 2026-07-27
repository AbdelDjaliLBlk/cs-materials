# -----------TD9 : Méthode Hongroise -----------
from colorama import Fore,Style # if not installed --> pip install colorama
import copy
def afficher_tableau(a,titre = None,x_char = None , y_char = None):
    #---Inside Functions---
    def legend_hongroise(a,x_char,y_char):
        x_l = [f"{x_char}{i}" for i in range(1,len(a[0])+1)]
        x_l.insert(0," ")
        y_l = [f"{y_char}{i}" for i in range(1,len(a)+1)]
        return x_l , y_l
    
    #----Variable----
    n = len(a)
    m  = len(a[0])
    l = 0 # Used to add a column for the legend 'x'
    if x_char and y_char:
        x,y = legend_hongroise(a,x_char,y_char)
        max_width = max(max([(len(f"{a[i][j]:.2f}")) for i in range(n) for j in range(m)]),len(x[0]),len(y[0]))
        l = 1
    else:
        max_width = max([(len(f"{a[i][j]:.2f}")) for i in range(n) for j in range(m)])
    
    #-------Titre-------
    if titre:
        for space in range(m+1):
            print("  ",end="")
        print(Fore.GREEN + titre+ Style.RESET_ALL)
    #-----Affichage-----
    def draw_line():
        for _ in range(m+l):
            print("+",end="")
            for __ in range(max_width+1):
                print("-",end="")
        print("+")
    
    draw_line()
    if x:
        for i in range(m+l):    
            print(f"| {x[i]:>{max_width-1}}" ,end=" ")
            if i ==m:
                print("|")
        draw_line()
    for i in range(n):
        if y:
            print(f"| {y[i]:>{max_width-1}}" ,end=" ")
        for j in range(0,m):
            if a[i][j] != 0 :
                print(f"| {a[i][j]:>{max_width}.2f}",end="")
            else:
                print(f"| {Fore.LIGHTYELLOW_EX}{a[i][j]:>{max_width}.2f}{Style.RESET_ALL}",end="")
            if j == m-1:
                print("|")
                draw_line()
def methode_hongroise(t,x_char = None ,y_char = None):
    # ---Variables---
    n = len(t)
    m = len(t[0])
    a = copy.deepcopy(t)
    max_cout = max(a[i][j] for i in range(n) for j in range(m))

    afficher_tableau(a1," Initial:",x_char,y_char) 
    # ---Réduction Ligne---
    for i in range(n):
        for j in range(m):
            a[i][j] = max_cout - a[i][j]
    for i in range(n):
        min_cout = min(a[i])
        for j in range(m):
            a[i][j] -= min_cout # Réduction Ligne
    afficher_tableau(a,"Réduction Ligne:",x_char,y_char)

    # ---Réduction Colonne---
    for j in range(m):
        column = [row[j] for row in a]
        min_cout = min(column)
        for i in range(n):
            a[i][j] -= min_cout # Réduction Colonne
    afficher_tableau(a,"Réduction Colonne:",x_char,y_char)

    # ---Choix Elements---
    assigned = {}       # dictionnaire ligne -> colonne
    rows_done = set()
    cols_done = set()

    while len(assigned) < n:
        # Zéros exclusifs par ligne
        for i in range(n):
            if i in rows_done:
                continue
            zero_cols = [j for j in range(m) if a[i][j] == 0 and j not in cols_done]
            if len(zero_cols) == 1:
                col = zero_cols[0]
                assigned[i] = col
                rows_done.add(i)
                cols_done.add(col)
        
        # Zéros exclusifs par colonne
        for j in range(m):
            if j in cols_done:
                continue
            zero_rows = [i for i in range(n) if a[i][j] == 0 and i not in rows_done]
            if len(zero_rows) == 1:
                row = zero_rows[0]
                assigned[row] = j
                rows_done.add(row)
                cols_done.add(j)

        # Affichage des affectations
        print(Fore.CYAN + "Affectation finale (ligne -> colonne):" + Style.RESET_ALL)
        for row, col in assigned.items():
            print(f"Ouvrier {row+1} → Poste {col+1}  | Rendement = {t[row][col]}")

        # Calcul du rendement total
        total = sum(t[row][col] for row, col in assigned.items())
        print(Fore.GREEN + f"Rendement total maximal = {total}" + Style.RESET_ALL)
        
if __name__ == "__main__":
    # -------Exo 1 -------
    # Maximiser le rendement total des ouvriers ?
    a1 = [ [24,22,19,0],
          [0,21,0,15],
          [18,0,20,19],
          [21,0,22,0]]
    methode_hongroise(a1,'T','0')

    # -------Exo 2 -------
    # Trouver l'affectation minimale ?
    
    """
    a2 = [ [9,8,6,4,6],
          [3,6,6,7,4],
          [4,9,8,3,6],
          [7,6,4,4,7],
          [2,8,3,5,6]
    ]
    afficher_tableau(a2,"Exo2:")
    """
