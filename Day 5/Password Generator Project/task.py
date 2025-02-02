import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


random_choices = ['l', 's', 'n']

total_len_password = nr_numbers + nr_letters + nr_symbols
unique_password = ""

while True :
    choice = random.choice(random_choices)
    if choice == 'l':
        if nr_letters > 0:
            unique_password = unique_password + random.choice(letters)
            nr_letters -= 1
    elif choice == 's':
        if nr_symbols > 0:
            unique_password = unique_password + random.choice(symbols)
            nr_symbols -= 1
    elif choice == 'n':
        if nr_numbers > 0:
            unique_password = unique_password + random.choice(numbers)
            nr_numbers -= 1
    if len(unique_password) == total_len_password:
        break

print(unique_password)

