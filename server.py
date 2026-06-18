import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clients = []
usernames = {}
username_to_conn = {}

# Dynamic chat rooms
rooms = {}
user_rooms = {}


def handle_client(conn, addr):
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break

            # ===== PRIVATE MESSAGE =====
            if message.startswith("/msg"):
                try:
                    parts = message.split()
                    target_user = parts[1]
                    private_message = " ".join(parts[2:])

                    if target_user in username_to_conn:
                        target_conn = username_to_conn[target_user]

                        target_conn.send(f"[PRIVATE] {usernames[conn]}: {private_message}".encode())
                        conn.send(f"[PRIVATE to {target_user}] {private_message}".encode())
                    else:
                        conn.send("User not found".encode())

                except:
                    conn.send("Invalid command. Use /msg username message".encode())

            # ===== JOIN / CREATE ROOM =====
            elif message.startswith("/join"):
                try:
                    new_room = message.split()[1]

                    # create room if not exists
                    if new_room not in rooms:
                        rooms[new_room] = []

                    # remove from old room
                    old_room = user_rooms[conn]
                    if conn in rooms[old_room]:
                        rooms[old_room].remove(conn)

                    # add to new room
                    rooms[new_room].append(conn)
                    user_rooms[conn] = new_room

                    conn.send(f"You joined {new_room}".encode())
                    print(f"{usernames[conn]} moved to {new_room}")

                except:
                    conn.send("Invalid command. Use /join room_name".encode())

            # ===== NORMAL MESSAGE =====
            else:
                room = user_rooms[conn]

                print(f"[{room}] {usernames[conn]}: {message}")

                for client in rooms[room]:
                    if client != conn:
                        client.send(f"[{room}] {usernames[conn]}: {message}".encode())

        except:
            print(f"[DISCONNECTED] {usernames.get(conn, 'Unknown')}")

            if conn in clients:
                clients.remove(conn)

            # remove from room
            if conn in user_rooms:
                room = user_rooms[conn]
                if conn in rooms.get(room, []):
                    rooms[room].remove(conn)

            conn.close()
            break


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[STARTED] Server running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()

        # get username
        username = conn.recv(1024).decode()
        usernames[conn] = username
        username_to_conn[username] = conn
        clients.append(conn)

        # default room
        if "main" not in rooms:
            rooms["main"] = []

        rooms["main"].append(conn)
        user_rooms[conn] = "main"

        print(f"[NEW USER] {username} joined (main)")

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


start_server()