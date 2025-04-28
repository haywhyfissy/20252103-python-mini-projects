import random

small_letters = list(map(chr, range(ord('a'), ord('z') + 1)))
capital_letters = list(map(chr, range(ord('A'), ord('Z') + 1)))
numbers = list(map(str, range(0, 10)))
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

password = []

password_length = int(input('Enter the length of the password: \n'))
num_small_letter = int(input('Enter the number of small letters: \n'))
num_capital_letter = int(input('Enter the number of capital letters: \n'))
num_number = int(input('Enter the number of numbers: \n'))
num_symbols = password_length - (num_small_letter + num_capital_letter + num_number)

i = 0
while i < num_small_letter:
    password.append(random.choice(small_letters))
    i += 1

j = 0
while j < num_capital_letter:
    password.append(random.choice(capital_letters))
    j += 1

k = 0
while k < num_number:
    password.append(random.choice(numbers))
    k += 1

l = 0
while l < num_symbols:
    password.append(random.choice(symbols))
    l += 1

final_password = random.sample(password, len(password))

print(f"Your password is: {''.join(final_password)}")

 