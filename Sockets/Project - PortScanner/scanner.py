import socket
import sys
from datetime import datetime
import threading


#Function to scan ports
def scan_port(target, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = client_socket.connect_ex((target, port))
    if result == 0:
        print("Port {} is open".format(port))
    client_socket.close()

#Main function
def main():
    # Define our target
    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])

    else:
        print("Invalid amount of arguments.")
        print("Usage: py scanner.py <ip>")
        sys.exit()

    # Add a pretty banner
    print("-" * 50)
    print("Scanning target " + target)
    print("Time started: " + str(datetime.now()))
    print("-" * 50)
    try:
        # Use a set to keep track of scanned ports
        scanned_ports = set()
        threads = []

        for port in range(1, 65536):
            if port not in scanned_ports:
                thread = threading.Thread(target=scan_port, args=(target, port))
                threads.append(thread)
                thread.start()
                scanned_ports.add(port)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()
            

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

    # Add a pretty banner   
    print("-" * 50)
    print("Time finished: " + str(datetime.now()))
    print("-" * 50)

if __name__ == "__main__":
    main()

