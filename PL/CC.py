import matplotlib.pyplot as plt
import numpy as np

#Définir les limites
x = np.linspace(0,600,500)

y1 = 500-x
y2 = (300-0.8*x)/0.3
y3 = (100-0.2*x)/0.7
y4 = (200-0.2*x)/0.7

y_lower = np.maximum(np.maximum(y1,y2),y3)
y_upper = y4
#condition d'existence
mask = y_upper >= y_lower

plt.plot(x,y1,'r',label='x+y=500')
plt.plot(x,y2,'g',label='0.8x+0.3y=300')
plt.plot(x,y3,'y',label='0.2x+0.7y=100')
plt.plot(x,y4,'b',label='0.2x+0.7y=200')

plt.fill_between(x,y_lower,y_upper,where=mask,alpha=0.2)

#Personalisation
plt.title("CC.")
plt.legend()
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0,600)
plt.ylim(0,700)
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
#Z = [100*x+200*y for(x,y) in points]
#print("-->Maximum Z = ",max(Z))
