import socket 
import sys

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 9999

# Connect to the server
client_socket.connect((host, port))

# Send data
message = "Hello, World!"
client_socket.sendall(message.encode())

# Receive data
data = client_socket.recv(1024)
print("Received:", data.decode())

# Close the connection
client_socket.close()
