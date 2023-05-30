import socket
import tkinter as tk

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Receive the random number from the server
number = int(client_socket.recv(1024).decode())

# Initialize the GUI
root = tk.Tk()
root.title('Guess the Number')

# Create a label and entry field for the guess
tk.Label(root, text='Guess the number between 1 and 100:').grid(row=0, column=0)
guess_entry = tk.Entry(root)
guess_entry.grid(row=0, column=1)

# Create a label to display the server's response
response_label = tk.Label(root, text='')
response_label.grid(row=1, column=0, columnspan=2)

# Create a function to handle the submit button
def submit_guess():
    # Get the guess from the entry field
    guess = int(guess_entry.get())
    
    # Send the guess to the server
    client_socket.send(str(guess).encode())
    
    # Receive the server's response
    response = client_socket.recv(1024).decode()
    
    # Display the response in the label
    response_label.config(text=response)
    
    # Check if the game is over
    if response.startswith('Congratulations'):
        # Disable the entry field and submit button
        guess_entry.config(state='disabled')
        submit_button.config(state='disabled')
    elif response == 'Higher' or response == 'Lower':
        # Clear the entry field
        guess_entry.delete(0, tk.END)
    
    # Decrement the number of guesses
    global guesses
    guesses -= 1
    
    # Check if the player has run out of guesses
    if guesses == 0:
        response_label.config(text='Game over. The number was ' + str(number))
        guess_entry.config(state='disabled')
        submit_button.config(state='disabled')

# Create a submit button
submit_button = tk.Button(root, text='Submit', command=submit_guess)
submit_button.grid(row=0, column=2)

# Initialize the number of guesses
guesses = 10

# Start the GUI
root.mainloop()

# Close the connection
client_socket.close()