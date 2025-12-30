#----------------Functions-----------------
def bubble_sort_asc(list):    
    n = len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j] , list[j+1] = list[j+1] , list[j]
def bubble_sort_desc(list):    
    n = len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] < list[j+1]:
                list[j],list[j+1] =list[j+1],list[j]
def afficher_matrice(a,n,m,y = None):
    n = len(a)
    max_width = 0
    num = [x for x in range(1,m)]
    for i in range(n):
        for j in range(m):
            max_width = max(max_width, len(f"{a[i][j]:.1f}"))
    print("         ",end="")
    for x in (num):
        print(f"{x:>{max_width}}", end=" ")
    print()
    for i in range(n):
        if y :
            print(f"{y}{i+1}: ",end="")
        print("[", end="")
        for j in range(m):
            print(f"{a[i][j]:>{max_width}.1f}", end="")
            if j < m - 1:
                print(" ", end="")
        print(" ]  ")
def lire_objets():
    num_art = int(input("Entrez le nombre d'objets :"))
    articles = {}
    for i in range(num_art):
        print(f"Articles {i+1} :")
        poids = int(input("Poids :"))
        valeur = int(input("Valeur :"))
        articles[i]= {
            "article":i+1,
            "poids": poids,
            "valeur":valeur
        }  
    return articles
def algorithme_glouton(capacite,articles):
    ratios = [(articles[i]["valeur"]/articles[i]["poids"], articles[i]) for i in range(len(articles))]
    bubble_sort_desc(ratios)

    min_poids = 0
    max_valeur = 0
    res = []
    for ratio, art in ratios:
        if min_poids + art["poids"] <= capacite:
            min_poids += art["poids"]
            max_valeur += art["valeur"]
            res.append([art["article"]])
    max_ration = sum([r for r, a in ratios if a["poids"] <= capacite])

    print("---------------Algorithme Glouton------------------")    
    print("* Valeur Max = ", max_valeur)
    print("** Poids Min = ", min_poids)
    print("*** Objets = ", res)
    print("**** Ratio Max = ", max_ration)
    return res
def programmation_dynamique(capacite,articles):  
    n = len(articles)
    print("-------------Programmation Dynamique-------------") 
    d = [[0 for j in range(capacite)] for i in range(n)]
    chosen = [[[] for j in range(capacite)] for i in range(n)]  

    for i in range(n):
        for j in range(capacite):
            if j+1 >= articles[i]["poids"]:
                d[i][j] = articles[i]["valeur"]
                chosen[i][j] = [articles[i]["article"]]  
                poids_i = articles[i]["poids"]
                for k in range(0, n):
                    if k != i:
                        if poids_i + articles[k]["poids"] <= j+1:   
                            poids_i += articles[k]["poids"]
                            d[i][j] += articles[k]["valeur"]
                            chosen[i][j].append(articles[k]["article"])

    max_val = 0
    max_articles = []
    for i in range(n):
        for j in range(capacite):
            if d[i][j] > max_val:
                max_val = d[i][j]
                max_articles = chosen[i][j]

    print("* Valeur Max =", max_val)
    print("** Objets =", max_articles)
def floyd_warshall(graph):
    # Collect all nodes (keys and destinations)
    nodes = set(graph.keys())
    for edges in graph.values():
        for v, _ in edges:
            nodes.add(v)
    nodes = list(nodes)

    # Initialize distance matrix
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}
    for u in nodes:
        dist[u][u] = 0
    for u in graph:
        for v, w in graph[u]:
            dist[u][v] = w

    # Floyd-Warshall
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

#----------------Main-----------------
if __name__ == "__main__":
    #Exo1
    capacite = int(input("Entrez la capacité du sac:"))
    articles = lire_objets()     
    algorithme_glouton(capacite,articles)
    programmation_dynamique(capacite,articles)
    #Exo2
    graph = {
    1: [(2, 2), (8, 8), (5, 5), (3, 3)],
    2: [(5, 5), (2, 1)],
    3: [(4, 2)],
    4: [(3, 3)],
    5: [(9, 9), (1, 1), (4, 3)]
    }
    dist = floyd_warshall(graph)
    print("Distance matrix (shortest paths):")
    for u in dist:
        print(u , "-->",dist[u])