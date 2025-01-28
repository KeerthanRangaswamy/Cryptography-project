import random
from sympy import isprime

def generate_prime(bits=512):
    p = random.getrandbits(bits)
    while not isprime(p):
        p = random.getrandbits(bits)
    return p

def generate_keypair(bits=512):
    p = generate_prime(bits)
    e1 = random.randint(2, p - 1)  
    d = random.randint(2, p - 2) 
    e2 = pow(e1, d, p)
    return (p, e1, e2), (p, e1, d)

def encrypt(public_key, P):
    p, e1, e2 = public_key
    ciphertext = []
    for char in P:
        m = ord(char) 
        r = random.randint(2, p - 2) 
        c1 = pow(e1, r, p) 
        c2 = (m * pow(e2, r, p)) % p 
        ciphertext.append((c1, c2))
    return ciphertext

def decrypt(private_key, ciphertext):
    p, e1, d = private_key
    P = ""
    for c1, c2 in ciphertext:
        m = (c2 * pow(c1, p - 1 - d, p)) % p 
        P += chr(m)
    return P

if __name__ == "__main__":
    print("Generating ElGamal keys...")
    public_key, private_key = generate_keypair(bits=512)
    print("Public Key:", public_key)
    print("Private Key:", private_key)
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("\nEnter your choice (1/2/3): ")
        if choice == '1':
            P = input("\nEnter a message to encrypt: ")
            encrypted_message = encrypt(public_key, P)
            print("\nEncrypted Message:", encrypted_message)
        elif choice == '2':
            encrypted_message_input = input("\nEnter the encrypted message (format: (c1, c2) (c1, c2) ...): ")    
            encrypted_message_input = encrypted_message_input.strip()
            encrypted_message_input = encrypted_message_input.replace(") (", ") (") 
            encrypted_message_input = encrypted_message_input.strip('()')
            ciphertext = []
            for pair in encrypted_message_input.split(") ("):
                pair = pair.strip("()")
                c1, c2 = map(int, pair.split(","))
                ciphertext.append((c1, c2)) 
            decrypted_message = decrypt(private_key, ciphertext)
            print("\nDecrypted Message:", decrypted_message)
        elif choice == '3':
            print("\nExiting the program...")
            break
        else:
            print("\nInvalid choice, please try again.")
