import socket

# Adresse IP et port du serveur
adresse_serveur = '127.0.0.1'
port_serveur = 12345

# Crée un socket TCP/IP
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lie le socket à l'adresse et au port
serveur_socket.bind((adresse_serveur, port_serveur))

# Écoute les connexions entrantes (maximum 1 client)
serveur_socket.listen(1)

print(f"Attente de la connexion du client sur {adresse_serveur}:{port_serveur}...")

# Accepte la connexion du client
client_socket, client_address = serveur_socket.accept()

print(f"Connexion établie avec {client_address}")

while True:
    # Recevoir des données du client
    message = client_socket.recv(1024).decode('utf-8')
    
    if not message:
        break
    
    print(f"Message du client : {message}")

# Ferme la connexion avec le client
client_socket.close()