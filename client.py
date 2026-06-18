import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter your username: ")
client.send(username.encode())

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("Connection lost")
            client.close()
            break


def send_messages():
    while True:
        message = input()
        client.send(message.encode())


# Run both send and receive at same time
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()