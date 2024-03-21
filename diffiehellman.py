import random
 
# public keys are taken
# p is a prime number
# g is a primitive root of p
p = int(input('Enter a prime number : '))
g = int(input('Enter a number : '))
 
 
class A:
    def __init__(self):

        self.n = random.randint(1, p)     
 
    def public_key(self):

        return (g**self.n)%p
 
    def compute_secret(self, gb):

        return (gb**self.n)%p
 
 
class B:
    def __init__(self):
        # Generating a random private number selected for alice
        self.a = random.randint(1, p)
        # Generating a random private number selected for bob
        self.b = random.randint(1, p)
        self.arr = [self.a,self.b]
 
    def public_key(self, i):
        # generating public values
        return (g**self.arr[i])%p
 
    def compute_secret(self, ga, i):
        # computing secret key
        return (ga**self.arr[i])%p
 
 
alice = A()
bob = A()
attacker = B()
 

print(f'Alice selected random number : {alice.n}')
print(f'Bob selected random number : {bob.n}')

print("\n The attacker will now select values for tampering with key exchange")
print(f'attacker selected private number for Alice (c) : {attacker.a}')
print(f'attacker selected private number for Bob (d) : {attacker.b}')
 

ga = alice.public_key()
gb = bob.public_key()
gea = attacker.public_key(0)
geb = attacker.public_key(1)
print(f'Alice has public key: {ga}')
print(f'Bob has public key: {gb}')

print(f'attacker has public key value for Alice: {gea}')
print(f'attacker has public key value for Bob : {geb}')
 

sa = alice.compute_secret(gea)
sea = attacker.compute_secret(ga,0)
sb = bob.compute_secret(geb)
seb = attacker.compute_secret(gb,1)
print(f'Alice computed secret : {sa}')
print(f'attacker computed key for Alice : {sea}')
print(f'Bob computed secret : {sb}')
print(f'attacker computed key for Bob: {seb}')