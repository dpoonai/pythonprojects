import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8,' '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+']

print("Welcome to Password Generator")
project_letters = int(input("Please indicate the amount of letters that would like to use in your password? \n"))
project_numbers = int(input(f"Please indicate how many numbers that you would like in your password? \n"))
project_symbols = int(input(f"Please indicate the amount of symbols that you would like in your password? \n"))

password = ""
#User is able to choose up to 4 letters

for character in range (1, project_letters + 1):
    password += random.choice(letters)
    print(password)

for character in range(1, project_numbers + 1):
    password += random.choice(numbers)

for character in range(1, project_symbols + 1):
    password += random.choice(symbols)

print(f"Your password is: {password}")


