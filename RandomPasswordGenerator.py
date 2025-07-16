#OBJECTIVES :
"""
1. find user preferences (length, upper, specials, digits etc.)

2. ensure we have at least one of each type
3. length is valid
4. randomly pick characters upto length
"""

import random
import string
def generate_password():
    while True:
        try:
            length=int(input("Enter the desired password length: ").strip())
            if length < 4 or length > 12:
                print("Password length should be in between 4 and 12 characters!\n")
                continue
            break
        except ValueError:
            print("Enter a valid value!\n")

    include_uppercase=input("Include Uppercase letters? (Y/N): ").strip().lower()
    include_special=input("Include Special characters letters? (Y/N): ").strip().lower()
    include_digits=input("Include Digits letters? (Y/N): ").strip().lower()

    lower = string.ascii_lowercase
    upper=string.ascii_uppercase if include_uppercase =="y" else ""
    special = string.punctuation if include_special == "y" else ""
    digits = string.digits if include_digits == "y" else ""
    all_char=lower+upper+special+digits
    #print(all_char)
    if not all_char:
        print("No character type is selected, select at least one. ")
# to include at least one type of users choice
    required_char=[]

    if include_uppercase == "y":
        required_char.append(random.choice(upper))
    if include_digits == "y" :
        required_char.append(random.choice(digits))
    if include_special == "y":
        required_char.append(random.choice(special))

# fill the remaining

    remaining_length=length-len(required_char)
    password = required_char

    for _ in range(remaining_length):
        character= random.choice(all_char)
        password.append(character)

    random.shuffle(password)
    print(''.join(password))

generate_password()
