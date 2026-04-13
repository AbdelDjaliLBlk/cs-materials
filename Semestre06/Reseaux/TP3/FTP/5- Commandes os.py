import os # bibliotheque systeme
import time
# os.mkdir cree un repertoire courant
# cette boucle cree les repertoires "0" jusqu'a "5"
for i in range(5):
        
        os.mkdir(str(i))
# met le programme en pause pour 10sec
time.sleep(10)
# rmdir supprime un repertorie 
# cette boucle supprime les repertoires "0" jusqu'a "5"
for i in range(5):
        os.rmdir(str(i))
        
# os.listdir imprime les noms des repertoires/fichiers dans
# le repertoire courant
print(os.listdir("."))
# os.getcwd() est equivalente a pwd (imprime le chemin actuel)
print (os.getcwd())
# CD .. (retourne au repertoire parant)
os.chdir("..")
print ("########",os.getcwd(),os.listdir("."))
