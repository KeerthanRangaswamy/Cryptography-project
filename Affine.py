import math  

char_to_index = {chr(i + ord('A')): i for i in range(26)}
index_to_char = {i: chr(i + ord('A')) for i in range(26)}

def encryptAffine(input_text, k1, k2, modulus):
    input_text = "".join(input_text.split())
    encrypted_text = []
    if input_text.isalpha() and len(input_text) >= 1:
        for char in input_text:
            p = char_to_index[char.upper()]
            transformed_p = (k1 * p + k2) % modulus
            encrypted_text.append(index_to_char[transformed_p])
        return "".join(encrypted_text)
    else:
        return "An Error has occurred, please check input."

def decryptAffine(input_text, k1, k2, modulus):
    input_text = "".join(input_text.split())

    decrypted_text = []
    if input_text.isalpha() and len(input_text) >= 1:
        for inverse in range(modulus):
            if (inverse * k1) % modulus == 1:
                break

        for char in input_text:
            c = char_to_index[char.upper()]
            transformed_c = (inverse * (c - k2)) % modulus
            decrypted_text.append(index_to_char[transformed_c])
        return "".join(decrypted_text)
    else:
        return "An Error has occurred, please check input."

def main():
    modulus = 26  
    operation = input("Please Enter 'e' for encryption or 'd' for decryption: ").lower()
    is_valid = True
    if operation not in ['e', 'd']:
        print("Invalid input, please enter 'e' for encryption or 'd' for decryption.")
        is_valid = False
    else:
        try:
            k1 = int(input(f"Enter a k1 value between 1 and {modulus - 1}: "))
            k2 = int(input(f"Enter an k2 between 0 and {modulus - 1}: "))
            if not (1 <= k1 <= modulus - 1) or not (0 <= k2 <= modulus - 1):
                print("Multiplier and Offset values are out of valid range.")
                is_valid = False
            elif math.gcd(k1, modulus) != 1:
                print(f"The GCD of multiplier and {modulus} must be 1.")
                is_valid = False
        except ValueError:
            print("Invalid numeric input, please enter valid integers.")
            is_valid = False
    if is_valid:
        if operation == 'e':  
            plaintext = input("\nPlease enter the plaintext to encrypt: \n").strip()
            ciphertext = encryptAffine(plaintext, k1, k2, modulus)
            print("\nPlaintext (Original): " + plaintext)
            print("Ciphertext (Encrypted): " + ciphertext)
        elif operation == 'd':  
            ciphertext = input("\nPlease enter the ciphertext to decrypt: \n").strip()
            plaintext = decryptAffine(ciphertext, k1, k2, modulus)
            print("\nCiphertext (Original): " + ciphertext)
            print("Plaintext (Decrypted): " + plaintext)

if __name__ == "__main__":
    main()
