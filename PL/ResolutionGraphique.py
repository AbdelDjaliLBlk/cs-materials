import matplotlib.pyplot as plt
import numpy as np

#Définir les limites
x = np.linspace(-10,10)
y = np.linspace(-10,10)
X,Y = np.meshgrid(x,y)

#Contraintes
Z2 = 6-X-2*Y
Z3 = 4-X-Y
Z4 = 3-X
Z5 = X 
Z6 = Y

#Droites
plt.plot(x,(6-x)/2,label='x+2y=6')
plt.plot(x,4-x,label='x+y=4')
plt.axvline(3,label='x=3',color='r')

#Countour.
plt.contourf(X,Y,Z3,levels=[-np.inf,0],colors=['lightblue'])
plt.contourf(X,Y,Z2,levels=[-np.inf,0],colors=['lightblue'])
plt.contourf(X,Y,Z4,levels=[-np.inf,0],colors=['lightblue'])
plt.contourf(X,Y,Z5,levels=[-np.inf,0],colors=['lightblue'])
plt.contourf(X,Y,Z6,levels=[-np.inf,0],colors=['lightblue'])

#Contour des solutions Z.
h = np.linspace(0,3,num=100)
plt.plot(h,-0.5*h+0.5,color='g')
plt.plot(h,-0.5*h+1,color='g')
plt.plot(h,-0.5*h+1.5,color='g')
plt.plot(h,-0.5*h+2,color='g')
plt.plot(h,-0.5*h+2.5,color='g')
plt.plot(h,-0.5*h+3,color='g')

#Personalisation
plt.title("TP1.")
plt.legend()
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.axhline(0,color="black",linewidth=0.5)
plt.axvline(0,color="black",linewidth=0.5)
plt.show()

#Résolution
points = [
    (0,0),
    (0,3),
    (2,2),
    (3,1),
    (3,0)
    ]
Z = [2*x+y for(x,y) in points]
print("-->Maximum Z = ",max(Z))
