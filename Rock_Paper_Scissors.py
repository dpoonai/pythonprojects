import random 
user_pick = int(input("Which option do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n "))
computer_pick = random.randint(1, 3)
print(f"Computer chose {computer_pick}")

if user_pick >= 4 or user_pick < 0:
    print("You typed an incorrect/invalid number, you lose")
elif user_pick == 1 and computer_pick == 3:
    print("You win!")
elif computer_pick == 1 and user_pick == 3:
    print("Computer wins")
elif computer_pick > user_pick:
    print("Computer wins")
elif user_pick > computer_pick:
    print("You win!")
elif computer_pick == user_pick:
    print("Computer wins")



