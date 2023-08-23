import random
import string

def generate_password():
    password_length = int(input("Enter the length of the password: "))
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()_-+={}[]<>/?,. "
    password = "".join(random.choice(characters) for _ in range(password_length))
    return password

if __name__ == "__main__":
    password = generate_password()
    print("Your password is:", password)
