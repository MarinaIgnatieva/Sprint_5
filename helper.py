import random
import string


def generate_email():
    return f'MarinaIgnatieva23{random.randint(100, 999)}@ya.ru'


def generate_password(length=6):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

