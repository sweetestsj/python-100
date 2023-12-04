import random

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters=int(input("How many letters would you like in your password?"))
num_symbols=int(input("How many symbols would you like?"))
num_numbers=int(input("How many numbers would you like?"))

password=""

for i in range(num_letters):
    password += chr(97+random.randint(0,26))
for i in range(num_symbols):
    password += symbols[random.randint(0,len(symbols)-1)]
for i in range(num_numbers):
    password += str(random.randint(0,9))

print(password) 
char_list = list(password)
random.shuffle(char_list)
print(''.join(char_list))