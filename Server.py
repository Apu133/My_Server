# Importing necessary libabries
from socket import *
import sys

# Storing ip, host and port details in variables
host = gethostname()
ip = gethostbyname(host)
port = 1234

# Initialising socket
server = socket(AF_INET, SOCK_STREAM)
server.bind(('', port))

# Starting listening mode
server.listen()

try:
    # While we receive signal
    while True:
        # Accepting client socket and address details
        client, address = server.accept()
        # Sending msg to the client with utf-8 encryption
        client.send(bytes("Connection has established.".encode("utf-8")))
        # Receiving client msg and decoding utf-8 
        msg = client.recv(1024).decode("utf-8")
        # Printing the client msg
        print(msg)
        # Unless client send exit, do this
        while msg != "exit":
            message = input("Enter your message: ")
            client.send(bytes(message.encode("utf-8")))
            msg = client.recv(1024).decode("utf-8")
            print(msg)

        # Closing the client socket
        client.close()
        sys.exit()
    # Closing the server socket
    server.close()
    sys.exit()
except socket.error as e:
    # Printing the error info
    print(f"Error: {e}")
finally:
    # Closing the server socket
    server.close()
    sys.exit()
    
