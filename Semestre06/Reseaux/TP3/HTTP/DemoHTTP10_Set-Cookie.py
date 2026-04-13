import socket
s=socket.socket()
s.bind(("0.0.0.0",80))
s.listen(30)
contenu="<h1> Page HTML</h1>"
votre_cookie=input("Entrez la valeur de la variable votre_cookie: ")
header='HTTP/1.1 200 OK\r\nConnexion:close\r\nDate: Thu, 17 Jan 2019 13:18:42 GMT\r\nServer: Apache/2.4.37\r\nAccept-Ranges: bytes\r\nContent-Length: %d\r\nContent-Type: text/html\r\nSet-Cookie:%s\r\n\r\n'%(len(contenu),votre_cookie)
while True:
    con,_=s.accept()
    con.send(header.encode())
    con.send(contenu.encode())
    con.close()
    
