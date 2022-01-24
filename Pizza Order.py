print("Welcome to Pizza Deliveries!")
size = input("What size pizza do you want? Small, Medium, or Large ")
add_vegetables = input(" Do you want vegetables? Yes or No ")
extra_cheese = input("Do you want extra cheese? Yes or No ")

bill = 0

if size == "Small":
    bill += 10
elif size == "Medium":
    bill += 20
elif size == "Large":
    bill += 25

if add_vegetables == "Yes":
    if size == "Small":
        bill += 5
    else:
        bill += 6

if extra_cheese == "Yes":
    bill += 2

print(f"Your final bill is ${bill}")

