# Networking is one of the most important concepts in programming. Sockets are a fundamental
# building block that enable communication, and higher-level protocols like HTTP, SMTP, and 
# database protocols use sockets to power websites, emails, and data systems.


#importing socket moudle built in module
import socket

#configuration 
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = "utf-8"
DISCONNETED = 'exit'

#create TCP trasmission control protocol
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#binding server 
server.bind((HOST,PORT))

#start listen
server.listen()
print(f"[STARTED] Server is running on {HOST}:{PORT}")