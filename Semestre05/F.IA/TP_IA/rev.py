from collections import deque
myResearchSpace={
    1:[2, 3],
    2:[4, 5],
    3:[6, 7],
    4:[8],
    5:[],
    6:[9, 10],
    7:[],
    8:[],
    9:[],
    10:[]
}



def dfs_search(space,I,F):
    print("---DFS Search---")
    open = []
    closed = []
    OrdreVisite = []
    open.append(I)
    while open : 
        etat_dep = open.pop()
        closed.append(etat_dep)
        if etat_dep == F:
            return True,closed
        for i in space[etat_dep]:
            if i not in open and i not in closed:
                open.append(i)
    return False,closed
def bfs_search(space,I,F):
    print("---BFS Search---")
    open = deque()
    closed = []
    OrdreVisite = []
    open.append(I)
    while open : 
        etat_dep = open.popleft()
        closed.append(etat_dep)
        if etat_dep == F:
            return True,closed
        for i in space[etat_dep]:
            if i not in open and i not in closed:
                open.append(i)
    return False,closed
def dls_search():
    return
def ids_search():
    return
def genere_successeur(space,n):
    if n in space:
        return space[n]
    else:
        return []

if __name__ == "__main__":
    print("------------Révision------------")
    I = 1
    F = 8
    found , OrdreVisite = bfs_search(myResearchSpace,I,F)
    print(f"Etat({I})-->Etat({F}).\nFound: {found}.\nOrdre Visite: {OrdreVisite}.")