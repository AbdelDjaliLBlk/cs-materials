#---------------Contraint satisfaction problem---------------
from ortools.sat.python import cp_model
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

model = cp_model.CpModel()
def exo1():
    print("----------------Exo1------------------")
    x = model.NewIntVar(0, 10, 'x') 
    y = model.NewIntVarFromDomain(cp_model.Domain.FromValues([2, 3, 8]), 'y')
    z = model.NewIntVar(1, 8, 'z') 
    model.Add(x + y == 8)
    model.Add(x > y)
    model.Add(z +y <=x)
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    #---------------Solution-------------------
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print('x=',solver.Value(x),end="  , ")
        print('y=',solver.Value(y),end="  , ")
        print('z=',solver.Value(z))
    else:
        print('No solution found.')
def exo2():
    print("----------------Exo2------------------")
    model = cp_model.CpModel()

    colors = {
        0: "Rouge",
        1: "Vert",
        2: "Bleu"
    }
    A = model.NewIntVar(0,2, 'A')
    B = model.NewIntVar(0,2, 'B')
    C = model.NewIntVar(0,2, 'C')
    D = model.NewIntVar(0,2, 'D')
    E = model.NewIntVar(0,2, 'E')
    F = model.NewIntVar(0,2, 'F')

    model.Add(A != B)
    model.Add(A != F)
    model.Add(A != C)
    model.Add(B != C)
    model.Add(A != E)
    model.Add(B != D)
    model.Add(B != F)
    model.Add(E != C)
    model.Add(C != D)
    model.Add(E != D)
    model.Add(F != D)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print('A =', colors[solver.Value(A)],end="       ")
        print('B =', colors[solver.Value(B)])
        print('C =', colors[solver.Value(C)],end="       ")
        print('D =', colors[solver.Value(D)])
        print('E =', colors[solver.Value(E)],end="      ")
        print('F =', colors[solver.Value(F)])
    else:
        print('No solution found.')
def exo3():
    print("----------------Exo3------------------")
    T = model.NewIntVar(0,9,'T')
    W = model.NewIntVar(0,9,'W')
    O = model.NewIntVar(0,9,'O')
    F = model.NewIntVar(0,9,'F')
    U = model.NewIntVar(0,9,'U')
    R = model.NewIntVar(0,9,'R')

    model.AddAllDifferent(T,W,O,F,U,R)
    model.Add(200*T+20*W+2*O == 1000*F +100*O + 10*U +R )

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    #---------------Solution-------------------
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print('T=',solver.Value(T),end=" ")
        print('W=',solver.Value(W),end=" ")
        print('O=',solver.Value(O))
        print('F=',solver.Value(F),end=" ")
        print('O=',solver.Value(O),end=" ")
        print('U=',solver.Value(U),end=" ")
        print('R=',solver.Value(R))
        print(" TWO + TWO = FOUR.")
        print(f"--> {solver.Value(T)}{solver.Value(W)}{solver.Value(O)} + {solver.Value(T)}{solver.Value(W)}{solver.Value(O)} = {solver.Value(F)}{solver.Value(O)}{solver.Value(U)}{solver.Value(R)}")
    else:
        print('No solution found.')
def exo4():
    print("----------------Exo4------------------")
    H = model.NewIntVar(11,24,'H')
    K = model.NewIntVar(11,24,'K')
    L = model.NewIntVar(11,24,'L')
    O = model.NewIntVar(11,24,'O')
    Y = model.NewIntVar(11,24,'Y')


    model.AddAllDifferent(H,O,K,Y)
    model.Add(H - K < 8 )
    model.Add(L == H)
    model.Add(Y < L)
    model.Add(H - O > 10)
    
    X = model.NewIntVar(0,24,'X') 
    model.Add(X == H-O)
    model.AddModuloEquality(1,X,2)
    
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    #---------------Solution-------------------
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"H = {solver.Value(H)}ans.")
        print(f"K = {solver.Value(K)}ans.")
        print(f"L = {solver.Value(L)}ans.")
        print(f"O = {solver.Value(O)}ans.")
        print(f"Y = {solver.Value(Y)}ans.")            
    else:
        print('No solution found.')
def exo5():
    print("----------------Exo5------------------")
    Verte = model.NewIntVar(1,6,'Verte')#verte
    Bleue = model.NewIntVar(1,6,'Bleue')#bleu
    Orange = model.NewIntVar(1,6,'Orange')#orange
    Violette = model.NewIntVar(1,6,'Violette')#violet
    Rouge = model.NewIntVar(1,6,'Rouge')#rouge
    Jaune = model.NewIntVar(1,6,'Jaune')#jaune

    model.AddAllDifferent(Verte,Bleue,Rouge,Jaune,Violette,Orange)
    model.Add(Bleue == 1)
    b = model.NewBoolVar("b")
    model.Add(Verte == Jaune+1).OnlyEnforceIf(b)
    model.Add(Verte == Jaune -1).OnlyEnforceIf(b.Not())
    model.Add(Violette < Orange)
    model.Add(Rouge == Violette +1)
    
    solver = cp_model.CpSolver()
    status = solver.solve(model)
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"* Balle{Verte} --> Tasse {solver.Value(Verte)}.")
        print(f"* Balle {Bleue} --> Tasse {solver.Value(Bleue)}.")
        print(f"* Balle {Orange} --> Tasse {solver.Value(Orange)}.")
        print(f"* Balle {Violette}--> Tasse {solver.Value(Violette)}.")
        print(f"* Balle {Rouge} --> Tasse {solver.Value(Rouge)}.")
        print(f"* Balle {Jaune} --> Tasse {solver.Value(Jaune)}.")
    else:
        print('No solution found.')
def exo6():
    print("----------------Exo6------------------")
    n = 6
    x = [[model.NewIntVar(1,n*n, f"x_{i}_{j}") for j in range(n)] for i in range(n)]
    S = model.NewConstant(int(n*(n*n+1)/2))

    for i in range(n):
        model.Add(sum(x[i][j] for j in range(n)) == S)
    model.Add(sum(x[i][n - 1 - i] for i in range(n)) == S)
    model.Add(sum(x[j][j] for j in range(n)) == S)
    model.AddAllDifferent([x[i][j] for i in range(n) for j in range(n)])

    solver = cp_model.CpSolver()
    status = solver.solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"     *Cube Magique de {n}:")
        for i in range(n):
            print("+---" * n + "+---+")
            print("| " + " | ".join(f"{solver.Value(x[i][j])}" for j in range(n)) + " |")
        print("+---" * n + "+---+")
    else:
        print('No solution found.')
def exo7():
    n = 8
    fig,ax = plt.subplots(figsize=(n, n))
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor='#769656'))
            else:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor='#eeeed2'))

    queen = mpimg.imread("queen.png") 
    ax.set_title('Queens Problem Solution')

    x = [model.NewIntVar(0,n-1, f"x_{i}") for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            model.Add(x[i] + i != x[j] + j)
            model.Add(x[i] - i != x[j] - j)
    model.AddAllDifferent(x)
    
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    for i in range(n):
            s =solver.Value(x[i])
            ax.imshow(queen, extent=[s, s+1, i, i+1], zorder = 10) 
    plt.show()
def exo8():
    puzzle = [
    [0, 3, 0, 4, 0, 5, 0, 7, 0],
    [6, 2, 0, 0, 8, 0, 4, 0, 0],
    [7, 0, 0, 0, 0, 1, 0, 0, 9],
    [2, 0, 6, 0, 0, 3, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 3],
    [0, 1, 3, 6, 0, 0, 9, 5, 0],
    [0, 0, 8, 0, 4, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 9, 0, 5, 0, 3, 8, 2]
 ]
def exo9():
    n = 8
    fig,ax = plt.subplots(figsize=(n, n))
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor='#769656'))
            else:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor='#eeeed2'))

    cavalier = mpimg.imread("chess.png") 
    ax.set_title('Cavalier Euler Solution')

    solver = cp_model.CpSolver()
    status = solver.solve(model)

    ax.imshow(cavalier, extent=[4, 5, 6, 7], zorder = 10) 
    plt.show()

if __name__ == '__main__':   
    """
    exo1()
    exo3()
    exo4()
    exo5()
    exo6()
    exo2()
    exo8()
    exo9()
    """
    exo7()    
        
        
