import socket
import json
import threading
from datetime import datetime

class Client:
    def __init__(self, name):
        self.name = name
        self.host = socket.gethostname()
        self.port = 9999
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        self.client_socket.send(json.dumps({"from": self.name}).encode())

        threading.Thread(target=self.receive_messages, daemon=True).start()

        while True:
            msg = input("Enter your message: ")
            recipient = input("Who do you want to send to? ")
            msg_obj = {"from": self.name, "msg": msg, "time": str(datetime.now()), "to": recipient}

            self.client_socket.send(json.dumps(msg_obj).encode())
            if msg.lower() == "exit":
                break

        self.client_socket.close()

    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode()
                msg_obj = json.loads(msg)
                print(f"\n{msg_obj['from']}: {msg_obj['msg']}\n")
            except:
                break

if __name__ == "__main__":
    name = input("Enter your name: ")
    Client(name).connect()
