import socket
IP = "192.168.1.1"
PORT = 50000
MESSAGE = "Ey 192.168.1.1! tu ecoute le port 50000?"
print( "UDP target IP:", IP)
print( "UDP target port:", PORT)
print( "message:", MESSAGE)
#creation d'un socket UDP
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.sendto(MESSAGE.encode(), (IP, PORT))
