import socket
import threading

# Adresse IP et port du serveur
adresse_serveur = '192.168.0.36'
port_serveur = 10000

# Dictionnaire pour stocker les informations des clients
clients = {}

# Fonction pour gérer les connexions clients
def gerer_client(client_socket):
    # Demander au client de choisir un nom
    client_socket.send("Choisissez un nom : ".encode('utf-8'))
    nom_client = client_socket.recv(1024).decode('utf-8')
    print(f"{nom_client} a rejoint le serveur.")
    
    # Enregistrer les informations du client dans le dictionnaire
    clients[nom_client] = client_socket
    
    # Envoyer un message de reçu au client avec son nom
    message_recu = f"Bienvenue, {nom_client} ! Vous êtes connecté."
    client_socket.send(message_recu.encode('utf-8'))
    
    while True:
        # Recevoir des données du client
        message = client_socket.recv(1024).decode('utf-8')
        
        if not message:
            break
        
        print(f"Message de {nom_client} : {message}")
        
        # Diffuser le message à tous les clients connectés (sauf à l'expéditeur)
        for client in clients:
            if client != nom_client:
                try:
                    clients[client].send(f"{nom_client}: {message}".encode('utf-8'))
                except:
                    # En cas d'erreur lors de l'envoi, supprimer la connexion client
                    del clients[client]
                    continue
    
    # Supprimer les informations du client lorsqu'il se déconnecte
    del clients[nom_client]
    client_socket.close()
    print(f"{nom_client} s'est déconnecté.")

# Crée un socket TCP/IP
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lie le socket à l'adresse et au port
serveur_socket.bind((adresse_serveur, port_serveur))

# Écoute les connexions entrantes (maximum 10 clients)
serveur_socket.listen(10)

print(f"Attente de connexions de clients sur {adresse_serveur}:{port_serveur}...")

while True:
    # Accepter une nouvelle connexion client
    client_socket, client_address = serveur_socket.accept()
    
    # Démarrer un thread pour gérer le client
    client_thread = threading.Thread(target=gerer_client, args=(client_socket,))
    client_thread.start()
