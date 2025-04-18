import socket
import threading


def handle_client(conn, addr,i):
    print(f"S: Connessione stabilita con {i}")
    # Qui puoi gestire la comunicazione con il client
    data = conn.recv(1024)  # Ricevi dati dal client
    if data:
        print(f"S: Ricevuto dal client: {data.decode('utf-8')}")
        conn.sendall(b"S: Messaggio ricevuto, sono il server 1 in ascolto su 8080!")
    print(f"S: Client totali connessi sulla porta 8080: {i}")
    conn.close()



server = socket.socket()
server.bind(("0.0.0.0",8080))
server.listen()
print("S: In attesa di connessioni...")
i=0
while True:
    conn, addr = server.accept()  # si blocca finché qualcuno si collega
    i = i+1
    thread = threading.Thread(target=handle_client, args=(conn, addr,i))
    thread.start()

