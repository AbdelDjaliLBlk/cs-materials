MyResearchSpace = {
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

    def display(self):
        print(f"Nom: {self.name} , Parent: {self.parent}.\nChemin : {self.action}.")
def test_etat_final(node, F):
    return node.name in F
def genere_successeur(node):
    if node.name in MyResearchSpace:
        return [Node(name, parent=node, action='explorer') for name in MyResearchSpace[node.name]]
    return []
def getSolution(node):
    path = []
    current = node
    while current is not None:
        path.append(current.name)
        current = current.parent
    path.reverse()
    return path    
def dfs_search(I, F):
    open_stack = []
    closed = []
    ordreVisite = []
    open_stack.append(Node(I, None, "")) 
    while open_stack:
        N = open_stack.pop()
        ordreVisite.append(N.name)

        if test_etat_final(N, F):
            return True, ordreVisite, getSolution(N)
        else:
            closed.append(N)
            succ = genere_successeur(N)
            for s in succ:
                if s.name not in [x.name for x in open_stack] and s.name not in [x.name for x in closed]:
                    open_stack.append(s)

    return False, ordreVisite, []

# --- Main ---
found, ordreVisite, path = dfs_search('B', 'E')
print(" Trouvé:", found)
print(" Ordre de visite:", ordreVisite)
print(" Chemin solution:", path)
