# 💬 Computer Networking Project — Chat Application

## 📌 1. System Architecture

This application uses a **Client-Server Architecture**.

* The **server** manages all connections and message routing.
* Multiple **clients** connect to the server using TCP sockets.
* The server handles chat rooms and private messaging.

### 🔹 How it works:

1. Server starts and listens for connections.
2. Clients connect and send their username.
3. Server assigns users to a default room ("main").
4. Messages are routed through the server to other users.

Client(Leon) > Server > Client(Sam)

---

## 📡 2. Communication Protocol

The application uses a **custom text-based protocol over TCP**.

### Supported Commands:

* `/join room_name`
  → Join or create a chat room.

* `/msg username message`
  → Send a private message to a specific user.

* `message`
  → Send a message to all users in the same room.

Client → Server → Other Clients

Step 1: Client sends message
Step 2: Server receives message
Step 3: Server checks room or command
Step 4: Server forwards message to other Clients.

---

## 🔄 3. Network Communication Flow

1. Client connects to server.
2. Client sends username.
3. Server stores user connection.
4. Client sends messages or commands.
5. Server processes:

   * Broadcast to room
   * Send private message
   * Move user between rooms

---

## ⚙️ 4. Installation Guide

### Requirements:

* Python installed

### Steps:

1. Open terminal
2. Navigate to project folder:

```
cd Desktop\chat-app
```

3. Start server:

```
py server.py
```

4. Start clients (in separate terminals):

```
py client.py
```
5. Enter users' names 
---

## ▶️ 5. Usage

### Example:

* Join a room:

```
/join room1
```

* Send a message:

```
Hello Sam
```

* Private message:

```
/msg Sam How are you
```
/msg Sam How is school?
---

## 📊 6. Protocol Analysis

### Why TCP?

* Reliable communication
* Ensures messages arrive in order
* Handles connection management

### Advantages:

* Simple implementation
* Stable communication
* Supports multiple users

### Disadvantages:

* Server is a single point of failure
* Less scalable than peer-to-peer

---

## ✅ 7. Features Implemented

* Multi-user chat
* Multiple chat rooms
* Private messaging
* Real-time communication
* Error handling
* Threaded server

---
