import socket

# Configuration (must match server)

PORT = 5050
FORMAT = "utf-8"
DISCONNECTED = "exit"

# Use same method as server to get IP

SERVER = socket.gethostbyname(socket.gethostname())

# Create socket (TCP)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server

client.connect((SERVER, PORT))
print(f"[CONNECTED] Connected to server at {SERVER}:{PORT}")

# Communication loop

while True:
    # Send message
    message = input("You: ")
    client.send(message.encode(FORMAT))

    if message == DISCONNECTED:
        print("[DISCONNECTED] Closing connection...")
        break

    # Receive reply
    reply = client.recv(1024).decode(FORMAT)
    print(f"[SERVER]: {reply}")


# Close connection
client.close()
print("[CLIENT CLOSED]")
