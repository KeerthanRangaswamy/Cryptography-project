import random
from math import gcd
from sympy import randprime

def generate_prime(bits=1024):
    p = randprime(2**(bits-1), 2**bits)
    q = randprime(2**(bits-1), 2**bits)
    while p == q:
        q = randprime(2**(bits-1), 2**bits)
    return p, q

def generate_keypair(bits=1024):
    p, q = generate_prime(bits)
    n = p * q
    N = (p - 1) * (q - 1)
    e = random.randrange(2, N)
    while gcd(e, N) != 1:
        e = random.randrange(2, N)
    d = pow(e, -1, N)
    return ((e, n), (d, n))

def encrypt(public_key, P):
    e, n = public_key
    P_ints = [ord(char) for char in P]
    C = [pow(char, e, n) for char in P_ints]
    return C

def decrypt(private_key, C):
    d, n = private_key
    decrypted = [pow(char, d, n) for char in C]
    P = ''.join([chr(char) for char in decrypted])
    return P

if __name__ == "__main__":
    print("RSA keys...")
    public_key, private_key = generate_keypair(bits=512) 

    print("Public Key:", public_key)
    print("Private Key:", private_key)
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("\nEnter your choice : ")
        if choice == '1':
            message = input("\nEnter the message to encrypt: ")
            encrypted_message = encrypt(public_key, message)
            print("\nEncrypted Message:", encrypted_message)
        elif choice == '2':         
            encrypted_message_input = input("\nEnter the encrypted message : ")
            encrypted_message = list(map(int, encrypted_message_input.split()))
            decrypted_message = decrypt(private_key, encrypted_message)
            print("\nDecrypted Message:", decrypted_message)
        elif choice == '3':
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid choice, try again.")