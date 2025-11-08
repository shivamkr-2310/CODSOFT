#password generator
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
print("=== password generator ===")
try:
    length = int(input("enter desired password:"))
    if length <= 0:
       print("password length must be greater than zero.")
    else:
     password = generate_password(length)
     print("\nyour generated password is:",password)
except ValueError:
       print("please enter a valid number for password length.")