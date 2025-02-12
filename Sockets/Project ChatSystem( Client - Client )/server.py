import socket
import threading
import json

class Server:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 9999
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}  # Store client sockets by name

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"New connection from {addr}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        try:
            # First message should contain the client name
            client_name = json.loads(client_socket.recv(1024).decode())["from"]
            self.clients[client_name] = client_socket
            print(f"{client_name} connected.")

            while True:
                msg = client_socket.recv(1024).decode()
                if not msg:
                    break

                msg_obj = json.loads(msg)
                recipient = msg_obj["to"]

                if recipient in self.clients:
                    self.clients[recipient].send(msg.encode())
                else:
                    error_msg = json.dumps({"from": "server", "msg": "Recipient not available"})
                    client_socket.send(error_msg.encode())

        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()
            if client_name in self.clients:
                del self.clients[client_name]

if __name__ == "__main__":
    Server().start()
