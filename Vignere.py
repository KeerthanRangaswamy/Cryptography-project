from random import sample
from itertools import product as col

def vigenere(P, k, encrypt):
    lst_final = []
    code=list(P)
    j=0

    for i, char in enumerate(code):
        if char.isalpha():
            code[i]=k[(i+j)%len(k)]
            if encrypt:
                lst_final.append((ord(P[i])+ord(code[i])-65*2)%26) 
            else:
                lst_final.append((ord(P[i])-ord(code[i]))%26)
        else:
            lst_final.append(ord(char))  
            j-=1  
    for i, char in enumerate(code):
        if char.isalpha():
            lst_final[i]=chr(lst_final[i]+65)
        else:
            lst_final[i]=chr(lst_final[i])

    return ''.join(lst_final)

print("Vigenere cipher")
if input('Type e for Encryption and d for Decryption: ').lower()=='e':
    P = input('Enter the plain text: ').upper()
    k = input('Enter the key: ').upper()
    encrypt = True
    print(vigenere(P, k, encrypt))
else:
    P = input('Enter the encrypted text: ').upper()
    encrypt = False
    k = input('Enter the key: ').upper()
    print(vigenere(P, k, encrypt))
