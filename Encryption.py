import random
import string

chars=list(" "+ string.ascii_letters+string.punctuation+string.digits)
key=chars.copy()
random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

#ENCRYPT
my_text = input("Enter the message to encrypt: ")
encrypted_text = ""

for letter in my_text:
    index=chars.index(letter)
    encrypted_text+=key[index]

#print(f"The Original message is: {my_text}")
print(f"The encrypted message is: {encrypted_text}")

#DECRYPT

encrypted_text = input("Enter the message to encrypt: ")
my_text= ""

for letter in encrypted_text:
    index=key.index(letter)
    my_text+=chars[index]

#print(f"The encrypted message is: {encrypted_text}")
print(f"The Original message is: {my_text}")

