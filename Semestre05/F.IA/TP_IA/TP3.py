myResearchSpace = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A', 'E', 'F', 'G'],
    'E': [],
    'F': ['E', 'G'],
    'G': [],
}
# --- Functions ---
class Node:
    def __init__(self, name, parent, action):
        self.name = name 
        self.parent = parent 
        self.action = action
        self.depth = 0 if parent is None else parent.depth + 1
def gener_successeur(etat):
    if etat.name in myResearchSpace:
       listSucc = myResearchSpace[etat.name]
       if len(listSucc) > 0:
          return [Node(x,etat,"") for x in listSucc]
       else:
           return []
def test_etat_final(node, F):
    return node.name == F
def getSolution(N):
    solution=[]
    parent=N.parent
    if parent is not None: solution=[parent.name,N.name]
    else: return [N.name]
    while parent.parent:
        solution.insert(0,parent.parent.name)
        parent=parent.parent
    return solution
def dls_search(I, F, limit, ordreVisite):
    open = [Node(I,None,"")]
    closed = []
    while open:
        N = open.pop()
        if test_etat_final(N, F) :
            return True, ordreVisite, getSolution(N)
        ordreVisite.append(N.name)
        if N.depth < limit:
            succ = gener_successeur(N)
            for s in succ:
                if s.name not in [x.name for x in open] and s.name not in [x.name for x in closed]:
                    open.append(s)
        closed.append(N)
    return False, ordreVisite, []
def dls_search_rec(N, F, limit, ordreVisite):
    ordreVisite.append(N.name)
    if test_etat_final(N, F):
        return True, ordreVisite, getSolution(N)
    if limit == 0:
        return False, ordreVisite, []
    for s in gener_successeur(N):
        found, ordreVisite, path = dls_search_rec(s, F, limit - 1, ordreVisite)
        if found:
            return True, ordreVisite, path
    return False, ordreVisite, []
def ids_search(I,F):
    max = 10
    for depth in range(max + 1):
        ordreVisite = []
        found, ordreVisite, path = dls_search(Node(I,None,""), F, depth, ordreVisite)
        print(f"Depth limit = {depth} | Visited = {ordreVisite}")
        if found:
            return True, ordreVisite, path
    return False, ordreVisite, []   

# --- Main ---
found, ordreVisite, path = dls_search('A','C',2,[])
print(" Trouvé:", found)
print(" Ordre de visite:", ordreVisite)
print(" Chemin solution:", path)

found, ordreVisite, path = ids_search('A','G')