from collections import deque

#---Functions---
MyResearchSpace={
 'A': ['B'],
 'B': ['C','D'],
 'C': ['D'],
 'D': ['A','E','F','G'],
 'E': [],
 'F': ['E','G',],
 'G': [],
 }
def genere_succeseur(etat):
    if etat in MyResearchSpace:
        return MyResearchSpace[etat]
    else:
        return []
def test_etat_final(etat,liste):
    return etat in liste
def parcours_profondeur(etat_init):
    open = []
    closed = []
    open.append(etat_init)
    print("Parcours en Profondeur:")
    while open:
        etat_dep = open.pop()
        closed.append(etat_dep)
        print(f"{etat_dep}-->{genere_succeseur(etat_dep)}.")
        for i in MyResearchSpace[etat_dep]:
            if i not in open and i not in closed:
                open.append(i)
def search(I,F):
    open = []
    closed = []
    open.append(I)
    while open:
        etat_dep = open.pop()
        closed.append(etat_dep)
        if(test_etat_final(etat_dep,F)):
            return True
        for i in MyResearchSpace[etat_dep]:
            if i not in open and i not in closed:
                open.append(i)
    return False
def search_fifo(I,F):
    open = deque()
    closed = []
    open.append(I)
    while open:
        etat_dep = open.popleft()
        closed.append(etat_dep)
        if(test_etat_final(etat_dep,F)):
            return True
        for i in MyResearchSpace[etat_dep]:
            if i not in open and i not in closed:
                open.append(i)
    return False
def chemin_arrive(etat_init , etat_fin):
    open = []
    closed = []
    open.append(etat_init)
    while open:
        etat_dep = open.pop()
        closed.append(etat_dep)
        if etat_fin in MyResearchSpace[etat_dep]:
                closed.append(etat_fin)
                return closed
        for i in MyResearchSpace[etat_dep]: 
            if i not in open and i not in closed:
                open.append(i)
    print(f"Aucun chemin trouvé entre {etat_init} et {etat_fin}.")

if __name__ == '__main__':
    #---Main---
    print(" D-->",genere_succeseur('D'))
    parcours_profondeur('A')
    #---Recherche---
    print("Chercher en profondeur : ",search('A',['G']))
    print("Chercher en largeur : ",search_fifo('A',['G']))
    #---Chemin---
    a = 'A';b = 'G'
    print(f"{a}-->{b} :",chemin_arrive(a,b))
