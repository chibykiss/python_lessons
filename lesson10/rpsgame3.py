import sys
import random
from enum import Enum

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3


    playerchoice = input("\nEnter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("Invalid input. Please enter 1, 2, or 3.")
        return play_rps()
    
    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose: " + str(RPS(player).name) + ".\n")
    print("Computer chose: " + str(RPS(computer).name + ".\n"))

    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😳 It's a tie!")    
    else:
        print("🐍 Computer wins!")

    print("\n Play again?")

    while True:
        playagain = input("\n Enter 'Y' to play again \n or 'Q' to quit:\n").lower()
        if playagain not in ['y', 'q']:
            continue
        else:
            break
    
    if playagain == 'y':
        return play_rps()
    else:
        print("\n🎉 🎉 🎉 🎉")
        print("Thanks for playing!\n")
        sys.exit("Bye!!!")

play_rps()
 