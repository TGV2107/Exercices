import socket

# Adresse IP et port du serveur
adresse_serveur = '127.0.0.1'
port_serveur = 12345

# Crée un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se connecte au serveur
client_socket.connect((adresse_serveur, port_serveur))

while True:
    # Demande à l'utilisateur de saisir un message
    message = input("Entrez un message (ou 'exit' pour quitter) : ")
    
    if message == 'exit':
        break
    
    # Envoie le message au serveur
    client_socket.send(message.encode('utf-8'))

# Ferme la connexion avec le serveur
client_socket.close()