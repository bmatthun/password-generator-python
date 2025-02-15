import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
password = []
for number in range(1, nr_letters + 1):
    password.append(random.choice(letters))
symbols_of_psw = []
for number in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))
numbers_of_psw = []
for number in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

print(password)

#Hard Level - Order of characters randomised:
mixed_psw = []
while len(mixed_psw) != len(password):
    random_index = random.randint(0, len(password) - 1)
    if random_index not in mixed_psw:
        mixed_psw.append(random_index)

for index_of_result in range(0, len(mixed_psw)):
    mixed_psw[index_of_result] = password[mixed_psw[index_of_result]]

print(mixed_psw)