import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + "@#%~*"
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

print("Сгенерированный пароль:", generate_password())