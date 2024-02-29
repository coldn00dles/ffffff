from rsabase import generate_key_pair, encrypt, decrypt
import random
# Test RSA encryption and decryption with randomly generated values
def test_rsa_encryption_decryption():
    # Generate key pair
    public_key, private_key = generate_key_pair()

    # Generate a random numeric plaintext
    plaintext = random.randint(1, 1000)

    # Encrypt the numeric plaintext
    ciphertext = encrypt(plaintext, public_key)

    # Decrypt the ciphertext
    decrypted_text = decrypt(ciphertext, private_key)

    # Print the results
    print("Original Numeric Value:", plaintext)
    print("Encrypted Ciphertext:", ciphertext)
    print("Decrypted Numeric Value:", decrypted_text)

if __name__ == "__main__":
    test_rsa_encryption_decryption()
