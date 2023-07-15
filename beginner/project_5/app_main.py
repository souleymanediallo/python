# Instruction : password Generator

import random
import string

# Get the length of the password
def get_length():
    length = input("How long do you want your password to be? ")
    return int(length)

# Get the number of letters
def get_letters():
    letters = input("How many letters do you want in your password? ")
    return int(letters)

# Get the number of numbers
def get_numbers():
    numbers = input("How many numbers do you want in your password? ")
    return int(numbers)

# Get the number of symbols
def get_symbols():
    symbols = input("How many symbols do you want in your password? ")
    return int(symbols)

# Generate the password
def generate_password(length, letters, numbers, symbols):
    password = []
    for i in range(letters):
        password.append(random.choice(string.ascii_letters))
    for i in range(numbers):
        password.append(random.choice(string.digits))
    for i in range(symbols):
        password.append(random.choice(string.punctuation))
    random.shuffle(password)
    return "".join(password)

# Main function
def main():
    length = get_length()
    letters = get_letters()
    numbers = get_numbers()
    symbols = get_symbols()
    password = generate_password(length, letters, numbers, symbols)
    print(password)

if __name__ == "__main__":
    main()

