import matplotlib.pyplot as plt
import numpy as np

def print_solution(Z,x1,x2,v_min = 0):
    print("+---Solution---+")
    print(f"|    x1 = {x1}    |")
    print(f"|    x2 = {x2}    |")
    if v_min != 0 : 
        print(f"|    Z* = {min(Z)}    |")
    else:
        print(f"|    Z* = {max(Z)}    |")
    print("+--------------+")
    
#Définir les limites
x = np.linspace(0,7)
y = np.linspace(0,7)
X,Y = np.meshgrid(x,y)

#Contraintes
Z2 = 3.5-X
Z3 = 3.2-Y


#Droites
plt.axvline(3.5,label='x=3.5',color='r')
plt.axhline(3.2,label='y=3.2',color='orange')


#Countour.
plt.contourf(X,Y,Z3,levels=[-np.inf,0],colors=['lightblue'])
plt.contourf(X,Y,Z2,levels=[-np.inf,0],colors=['lightblue'])
plt.contourf(X,Y,X,levels=[-np.inf,0],colors=['lightblue'])
plt.contourf(X,Y,Y,levels=[-np.inf,0],colors=['lightblue'])

#Contour des solutions .
x1 = x2 = 0
Z = []
for i in range(0,4):
    for j in range(0,4):
        plt.scatter(i, j, s=20)
        Z.append(i+j)
        x1,x2 = i,j

print_solution(Z,x1,x2)
#Personalisation
plt.title("Branch&Bound")
plt.legend()
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0,7)
plt.ylim(0,7)
plt.axhline(0,color="black",linewidth=0.5)
plt.axvline(0,color="black",linewidth=0.5)
#plt.show()


