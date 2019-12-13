import random
import string


def password(length):
    password = str()

    for i in range(length - 2):
        password += random.choice(string.ascii_letters)

    password += random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '~'])
    password += str(random.choice(range(10)))
    return password


print(password(10))
