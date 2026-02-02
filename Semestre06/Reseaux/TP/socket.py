import socket
import sys

# Check mode: server or client
# Usage:
#   python socket_app.py server
#   python socket_app.py client
if len(sys.argv) != 2:
    print("Usage: python socket_app.py server|client")
    sys.exit()

mode = sys.argv[1]

HOST = "127.0.0.1"
PORT = 12345

# ===================== SERVER =====================
if mode == "server":
    # Create TCP socket (IPv4)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket to IP and port
    server_socket.bind((HOST, PORT))

    # Start listening for connections
    server_socket.listen(1)
    print("Server listening...")

    # Accept a client connection
    conn, addr = server_socket.accept()
    print("Connected by:", addr)

    # Receive data from client
    data = conn.recv(1024).decode()
    print("Client says:", data)

    # Send response
    conn.send("Hello from server".encode())

    # Close connections
    conn.close()
    server_socket.close()

# ===================== CLIENT =====================
elif mode == "client":
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((HOST, PORT))

    # Send message to server
    client_socket.send("Hello from client".encode())

    # Receive server response
    response = client_socket.recv(1024).decode()
    print("Server says:", response)

    # Close socket
    client_socket.close()

else:
    print("Invalid mode. Use 'server' or 'client'")
