import socket
from datetime import datetime

# Server Chat System

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 9999 # Port to listen on

# Bind to the port
server_socket.bind((host, port)) # Bind to the port

print("Server started on port", port)

# Wait for client connection
server_socket.listen(5)

while True:
    # Establish connection with client
    client_socket, addr = server_socket.accept()
    print('-'*50)
    print('Got connection from', addr)
    print('-'*50)
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        print('Client : ', data.decode())

        # Send data to the client
        message = input("Enter message: ")
        client_socket.sendall(message.encode()) 
        if data.decode() == 'exit':
            client_socket.close()
            break
    break