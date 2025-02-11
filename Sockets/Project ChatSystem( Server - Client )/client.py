import socket
from datetime import datetime

# Client Chat System    

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 9999

# Connect to the server
client_socket.connect((host, port))

try:
    while True:
        # Send data
        message = input("Enter message: ")  
        client_socket.sendall(message.encode())

        # Receive data
        data = client_socket.recv(1024)
        print('Server : ', data.decode())

        # Close the connection  
        if message.lower() == "exit":
            print("Closing connection...")
            client_socket.close()
            break
except Exception as e:
    print(f"An error occurred: {e}")
    client_socket.close()