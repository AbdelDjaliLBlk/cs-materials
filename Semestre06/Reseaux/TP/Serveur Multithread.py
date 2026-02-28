import socket
import _thread

def Traiter_Connexion(connexion_avec_client,adresse_client):
   MessageRec=""
   
   print( "Connexion de la machine = ", adresse_client)
   try:
      while(MessageRec.strip().lower()!="fin"):
          MessageRec=connexion_avec_client.recv(1024)
          MessageRec=MessageRec.decode()
          print( "Client" ,adresse_client," a dit :",MessageRec)
   except:
      print( "Deconnexion")
   print( "Deconnexion de :",adresse_client)
   try:
      connexion_avec_client.close()
   except:
      pass

SocketServeur = socket.socket()
host = socket.gethostname() 
port = 9500 
SocketServeur.bind(("127.0.0.1", port)) 

SocketServeur.listen(5)

print( "Lancement serveur")
while True:
   ConnexionAUnClient, addrclient = SocketServeur.accept() 
   _thread.start_new_thread(Traiter_Connexion,(ConnexionAUnClient,addrclient))

       

