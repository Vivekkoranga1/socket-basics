# Networking is one of the most important concepts in programming. Sockets are a fundamental
# building block that enable communication, and higher-level protocols like HTTP, SMTP, and 
# database protocols use sockets to power websites, emails, and data systems.


#importing socket moudle built in module
import socket

#configuration 
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = "utf-8"
DISCONNECTED = 'exit'

#create TCP trasmission control protocol
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#binding server 
server.bind((HOST,PORT))

#start listen
server.listen()
print(f"[STARTED] Server is running on {HOST}:{PORT}")

#Accepting the connections
conn,addr = server.accept()
print(f"[CONNECTED] {addr} connected.")

# communication between server and client
while True:
    message = conn.recv(1024).decode('utf-8')

    if not message:
        break

    print(f"[CLIENT]: {message}")

    # Send reply
    reply = input("You: ")
    conn.send(reply.encode('utf-8'))

#close the connection
conn.close()
