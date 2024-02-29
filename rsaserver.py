import socket
import pickle
from rsabase import getkeypairs, decrypt


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server listening!")

connection, address = server_socket.accept()
print("Connection from:", address)

pu_key, pr_key = getkeypairs()


connection.send(pickle.dumps(pu_key))


encrypted_data = connection.recv(1024)
ciphertext = pickle.loads(encrypted_data)

decrypted_text = decrypt(ciphertext, pr_key)

print("Received ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)
print("Sending decrypted text!")

connection.send(pickle.dumps(decrypted_text))

connection.close()
server_socket.close()


