import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to The PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

choices = [nr_letters, nr_symbols, nr_numbers]
# print(choices)
counter = 0
L = []
S = []
N = []

for i in range(nr_letters):
    letters_c = random.randint(0, 51)
    L.append(letters[letters_c])
L = "".join(L)

for i in range(nr_symbols):
    symbols_c = random.randint(0, 8)
    S.append(symbols[symbols_c])
S = "".join(S)

for i in range(nr_numbers):
    numbers_c = random.randint(0, 9)
    N.append(numbers[numbers_c])
N = "".join(N)

password = L + S + N
print(password)
print(''.join(random.sample(password, len(password))))

