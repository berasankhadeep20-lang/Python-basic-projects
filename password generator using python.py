#password generator using python
import random
def password_generator(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
n = int(input("Enter the desired password length: "))
print("Generated Password:", password_generator(n))