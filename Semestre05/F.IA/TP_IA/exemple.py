#---------------Contraint satisfaction problem---------------
from ortools.sat.python import cp_model
from colorama import Fore,Style
model = cp_model.CpModel()

def scheduling(n = 3):
    print(Fore.YELLOW + "-----Exam Scheduling-----" + Style.RESET_ALL)
    courses = ["MATH", "PHYS", "CS", "BIO", "CHEM"]

    MATH  = model.NewIntVar(1, n, "MATH")
    PHYS  = model.NewIntVar(1, n-1, "PHYS")
    CS    = model.NewIntVar(1, n, "CS")
    BIO   = model.NewIntVar(1, n, "BIO")
    CHEM  = model.NewIntVar(1, n, "CHEM")

    model.Add(MATH != PHYS)
    model.Add(MATH != CS)
    model.Add(PHYS != CS)
    model.Add(CS != BIO)
    model.Add(BIO != CHEM)
    model.Add(BIO > CHEM)
    #model.AddAllDifferent([MATH, PHYS , BIO , CS , CHEM])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    #---------------Solution-------------------
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"{Fore.GREEN}MATH{Style.RESET_ALL} = {solver.Value(MATH)}",end= "      ")
        print(f"  {Fore.GREEN}PHYS{Style.RESET_ALL} = {solver.Value(PHYS)}")
        print(f"{Fore.GREEN}CS{Style.RESET_ALL} = {solver.Value(CS)}",end= "         ")
        print(f"  {Fore.GREEN}BIO{Style.RESET_ALL} = {solver.Value(BIO)}")
        print(f"{Fore.GREEN}CHEM{Style.RESET_ALL} = {solver.Value(CHEM)}")
    else:
        print(Fore.RED + "ERROR : No solution found." + Style.RESET_ALL)

def simplexe():
    print(Fore.YELLOW + "-----Simplexe Method-----" + Style.RESET_ALL)
    model = cp_model.CpModel()

    x1 = model.NewIntVar(4, 100, 'x1')
    x2 = model.NewIntVar(0, 3, 'x2')

    model.Add( x1 + x2 >= 6)
    model.Add( x2 <= 3)

    model.Maximize(5*x1 + 7*x2)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"x1 = {Fore.GREEN}{solver.Value(x1)}{Style.RESET_ALL}",end= "      ")
        print(f"  x2 = {Fore.GREEN}{solver.Value(x2)}{Style.RESET_ALL}")
        print(f"Optimal value = {Fore.GREEN}{solver.ObjectiveValue()}{Style.RESET_ALL}")
    else:
        print(Fore.RED + "ERROR : No solution found." + Style.RESET_ALL)

if __name__ == '__main__':
    #scheduling()
    simplexe()