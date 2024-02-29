
import socket
import aessample 

def handle_client(client_socket):
    key = client_socket.recv(1024).decode('utf-8')
    print(f"Received key from client: {key}")

    plaintext = client_socket.recv(1024).decode('utf-8')
    print(f"Received plaintext from client: {plaintext}")
    encrypted_data = aessample.encryptor(key.encode('utf-8'), plaintext.encode('utf-8'))

    client_socket.send(encrypted_data)
    print("Encrypted data sent back to client.")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5555))
server_socket.listen(5)

print("Server listening on port 5555...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")

    handle_client(client_socket)

    client_socket.close()

