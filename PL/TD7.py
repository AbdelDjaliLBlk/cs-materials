import matplotlib.pyplot as plt
import numpy as np
def my_fct(capacite):
    articles = sorted(articles,key = lambda x:x["valeur"]/x["poids"],reverse =True)
    res = []
    i = 0
    c = capacite
    while capacite > 0 and i<len(articles):
        if capacite - articles[i]["poids"] >= 0:
            res.append(articles[i]["poids"])
            capacite -= articles[i]["poids"]
        else: 
            i = i+1
    print("---------------Algorithme Glouton------------------")        
    print("* Capacité = ",c,".\n**",end ="")
    valeur_t = 0
    for j in range(len(articles)):   
        occ =  list.count(res,articles[j]["poids"])
        if occ != 0:
            print(f" Article de valeur {articles[j]["valeur"]} ,{occ} fois.")
            valeur_t += articles[j]["valeur"] * occ
    print("*** Valeur Totale:",valeur_t)

# ==========================================
# NOUVEAU PROGRAMME LINÉAIRE
# ==========================================
# Max Z = x + y
# Contraintes:
# x ≤ 3.5
# y ≤ 3.2
# x, y ∈ N (entiers)
# ==========================================

# Créons des listes de valeurs entières possibles
x_vals = range(0, 4)   # x = 0, 1, 2, 3
y_vals = range(0, 4)   # y = 0, 1, 2, 3

# Liste pour stocker les points admissibles
points = []

# Recherche des solutions entières faisables
for x in x_vals:
    for y in y_vals:
        if x <= 3.5 and y <= 3.2:
            points.append((x, y))

# Calcul de Z pour chaque point faisable
Z_vals = [x + y for x, y in points]

# Trouver la valeur maximale et le point associé
Z_max = max(Z_vals)
best_point = points[Z_vals.index(Z_max)]

print("Points faisables :", points)
print("Valeur maximale de Z =", Z_max, "au point", best_point)

# ==========================================
# Tracé graphique
# ==========================================
plt.figure(figsize=(7,6))

# Contraintes
plt.axvline(x=3.5, color='orange', linestyle='--', label='$x=3.5$')
plt.axhline(y=3.2, color='green', linestyle='--', label='$y=3.2$')

# Zone faisable (rectangle)
plt.fill_between(np.linspace(0, 3.5, 100), 0, 3.2, color='lightblue', alpha=0.4, label='Zone faisable')

# Points entiers faisables
for (x, y) in points:
    plt.scatter(x, y, color='blue')

# Point optimal
plt.scatter(best_point[0], best_point[1], color='red', s=100, label=f'Optimum {best_point} (Z={Z_max})')

plt.xlim(0, 4)
plt.ylim(0, 4)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('TD7_Exo1')
plt.savefig("TD7_Exo1")
plt.show()
