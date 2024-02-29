import socket
import aessample

def get_input():
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")
    return key, plaintext

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5555))

key, plaintext = get_input()
key_bytes = key.ljust(16, '\x00').encode()[:16]
client_socket.send(key_bytes)
print("Key sent to server.")


client_socket.send(plaintext.encode('utf-8'))
print("Plaintext sent to server.")


encrypted_data = client_socket.recv(1024)


decrypted_data = aessample.decryptor(key_bytes, encrypted_data).decode('utf-8')
print(f"Decrypted data received from server: {decrypted_data}")

client_socket.close()

