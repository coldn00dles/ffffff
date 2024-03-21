import socket
from dhell import generate_prime, calculate_primitive_root, generate_key, calculate_shared_secret

# Specify the server's address and port
server_address = 'localhost'
server_port = 12345

# Create socket
attacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
try:
    attacker_socket.connect((server_address, server_port))
    print(f"Attacker: Connected to server at {server_address}:{server_port}")

    # Generate attacker's own prime and primitive root
    p_attacker = generate_prime()
    g_attacker = calculate_primitive_root(p_attacker)

    # Generate keys for attacker
    Xc, Yc = generate_key(p_attacker, g_attacker)

    # Send public key to server (as if it's the genuine client)
    attacker_socket.send(str(Xc).encode())
    print(f"Attacker: Sent Public Key to Server: {Xc}")

    # Receive server's public key (not the genuine client's)
    Xb_fake = int(attacker_socket.recv(1024).decode())
    print(f"Attacker: Received Server's (Fake) Public Key: {Xb_fake}")

    # Calculate shared secret (with the fake public key)
    shared_secret_fake = calculate_shared_secret(Yc, Xb_fake, p_attacker)
    print(f"Attacker: Calculated Shared Secret with (Fake) Server: {shared_secret_fake}")

except Exception as e:
    print(f"Attacker: Error - {e}")

finally:
    # Close connection
    attacker_socket.close()
