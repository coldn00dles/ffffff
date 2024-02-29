
import random
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primegen():
    prime_candidate = random.randint(1, 100)
    while not isPrime(prime_candidate):
        prime_candidate = random.randint(1, 100)
    return prime_candidate

def extgcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extgcd(b % a, a)
        return (g, y - (b // a) * x, x)

def multinverse(A, M):
    g, x, y = extgcd(A, M)
    if g != 1:
        return -1
    else:
        return x % M

def getkeypairs():
    p, q = primegen(), primegen()
    n = p * q
    prim = (p - 1) * (q - 1)

    e = random.randrange(2, prim)
    while extgcd(e, prim)[0] != 1:
        e = random.randrange(2, prim)

    d = multinverse(e, prim)

    if d == -1:
        print("Error: No multiplicative inverse found. Try a different encryption key.")
        return None

    return (n, e), (n, d)

def encrypt(pt, pukey):
    n, e = pukey
    ct = pow(pt, e, n)
    return ct

def decrypt(ct, privkey):
    n, d = privkey
    decrypted_text = pow(ct, d, n)
    return decrypted_text
