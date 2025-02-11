import socket
import datetime

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define our target
host = socket.gethostname()
port = 9999

# Print the time started
print("Time started: " + str(datetime.datetime.now()))

# Bind to the port
s.bind((host, port))

print("Server started on port", port) 

# Wait for client connection
s.listen(5)

while True:
    # Establish connection with client
    client_socket, addr = s.accept()
    print('Got connection from', addr)
    data = client_socket.recv(1024)
    print('Server received', data.decode())
    client_socket.sendall(data)
    client_socket.close()
    break

# Close the connection
s.close()

# Print the time finished
print("Time finished: " + str(datetime.datetime.now()))

