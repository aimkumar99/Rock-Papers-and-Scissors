print ("Welcome to Rock, Paper and Scissors Game!")
import random
import os
from arts import rock,paper,scissor
list = [rock, paper, scissor]
play_again = True
while play_again:
    os.system("cls")
    users_choice = input("What do you want to choose? rock, paper or scissor.\n").lower()
    if users_choice == "rock" or "paper" or "scissor":
        if  users_choice == "rock":
            print(f"You chose:")
            print(rock)
        elif  users_choice == "paper":
            print(f"You chose:")
            print(paper)
        elif  users_choice == "scissor":
            print(f"You chose:")
            print(scissor)

    if users_choice == "rock":
            users_choice = rock
    elif users_choice == "paper":
            users_choice = paper
    elif users_choice == "scissor":
            users_choice = scissor

    if users_choice == rock or users_choice == paper or users_choice == scissor:
        random_choice = random.choice(list)
        print(f"The computer chose:\n {random_choice}")
        if users_choice == random_choice:
            print("It's a draw. Play again.")
        elif users_choice == rock:
            if random_choice == paper:
                print("Sorry! You lose.")
            else:
                print("Congratulations! You win.")
        elif users_choice == paper:
            if random_choice == scissor:
                print("Sorry! You lose.")
            else:
                print("Congratulations! You win.")
        elif users_choice == scissor:
            if random_choice == rock:
                print("Sorry! You lose.")
            else:
                print("Congratulations! You win.")
    else:
        print("You typed an invalid choice. You lose.")
    decision = input("Do you want to play again? Type 'y' to replay, and 'n' to exit.\n").lower()
    if decision == "n":
         play_again = False
print("The game ended. Thank you for playing.")

    