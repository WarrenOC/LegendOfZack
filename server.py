import socket
import threading
import pickle

# Server settings
HOST = "0.0.0.0"  # Listen on all available IPs
PORT = 5555
players = {}  # Dictionary to store player positions

# Start the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)  # Allow up to 2 players
print("Server started, waiting for connections...")


def handle_client(conn, addr, player_id):
    print(f"New connection from {addr}, assigned Player {player_id}")
    players[player_id] = {"x": 50, "y": 50}  # Default spawn position

    while True:
        try:
            data = pickle.loads(conn.recv(1024))  # Receive data
            if not data:
                break
            players[player_id] = data  # Update player position
            conn.sendall(pickle.dumps(players))  # Send all player data back
        except:
            break

    print(f"Player {player_id} disconnected")
    del players[player_id]
    conn.close()


# Accept clients
player_id = 0
while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr, player_id)).start()
    player_id += 1
