import socket
import threading

# Adresse IP et port du serveur
adresse_serveur = '192.168.0.36'
port_serveur = 10000

# Crée un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se connecte au serveur
client_socket.connect((adresse_serveur, port_serveur))

# Demander au client de choisir un nom
nom_client = input("Choisissez un nom : ")
client_socket.send(nom_client.encode('utf-8'))

# Recevoir un message de reçu du serveur
message_recu = client_socket.recv(1024).decode('utf-8')
print(message_recu)

while True:
    # Demande à l'utilisateur de saisir un message
    message = input(f"{nom_client} - Entrez un message (ou 'exit' pour quitter) : ")
    
    if message == 'exit':
        break
    
    # Envoie le message au serveur
    client_socket.send(message.encode('utf-8'))

# Ferme la connexion avec le serveur
client_socket.close()
