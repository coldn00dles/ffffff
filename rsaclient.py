import socket
import pickle
from rsabase import encrypt


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))


PUKEY_data = client_socket.recv(1024)
PUKEY = pickle.loads(PUKEY_data)



plaintext = int(input("Enter plaintext to be encrypted"))
ciphertext = encrypt(plaintext, PUKEY)
client_socket.send(pickle.dumps(ciphertext))

n1,e1 = PUKEY
print("Received public key : ",e1)

decrypted_data = client_socket.recv(1024)
decrypted_text = pickle.loads(decrypted_data)

print("Received ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)

client_socket.close()


