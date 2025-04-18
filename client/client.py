import socket
import random


# 2. Connessione al server (IP e porta del server)
server_ip = 'nginx' #Nome del container in docker
server_port = [8080,8025]


for i in range(1,11):
    # 1. Crea il socket client
    client = socket.socket()
    porta = random.choice(server_port)
    print(f"C: Mi collego al server {server_ip}:{porta}...")
    client.connect((server_ip, porta))
    print("C: Connesso!")

    # 3. Mando un messaggio al server
    message = "C: Ciao dal client!"
    client.sendall(message.encode())
    print("C: Messaggio inviato!")

    # 4. Ricevo la risposta dal server
    response = client.recv(1024)
    print("C: Risposta dal server:", response.decode())

    # 5. Chiudo la connessione
    client.close()
    print("C: Connessione chiusa.")
    print()
