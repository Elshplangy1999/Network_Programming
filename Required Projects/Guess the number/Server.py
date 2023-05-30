import socket
import random

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Bind the socket to the host and port
server_socket.bind((host, port))

# Wait for client connection
server_socket.listen(1)
print('Waiting for a client connection...')

# Generate a random number
number = random.randint(1, 100)

# Accept client connection
client_socket, addr = server_socket.accept()
print('Connection established with', addr)

# Send the random number to the client
client_socket.send(str(number).encode())

# Play the game
guesses = 10
while guesses > 0:
    # Receive the guess from the client
    guess = int(client_socket.recv(1024).decode())
    
    # Compare the guess with the number and send a response
    if guess == number:
        client_socket.send(b'Congratulations! You guessed the number.')
        break
    elif guess < number:
        client_socket.send(b'Higher')
    else:
        client_socket.send(b'Lower')
    guesses -= 1

# Close the connection
client_socket.close()
server_socket.close()