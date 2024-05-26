#write python password generator using the random module
import random
import os, sys
print("Welcome to Python password generator")
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pass_lenght = int()

while pass_lenght < 12:
    print("For maximum security, your password MUST be longer than 12 symbols!!!")
    nr_letters = int(input("How many letters do you want your password to contain:\n "))
    nr_numbers = int(input("How many numbers do you want your password to contain:\n "))
    nr_symbols = int(input("How many symbols do you want your passwprd to contain:\n "))
    pass_lenght = nr_letters + nr_numbers + nr_symbols

os.system('clear')
password_list = []
pass_string = ""
print(f"The generated password will be {pass_lenght} characters long")

for letter in range(1, nr_letters+1):
    password_list.append(random.choice(letters))
for number in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))
for symbol in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))
        
random.shuffle(password_list)
for char in password_list:
    pass_string += char

print(f"Your Python generated password is: \n {pass_string} ")



