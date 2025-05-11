import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS(1))
# print(RPS.PAPER)
# print(RPS['ROCK'])
# print(RPS.ROCK.name)
# print(RPS.ROCK.value)
# sys.exit("Exiting the program")

# value = input('Please enter a value:\n')

# print(value)

print("")
playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter a number between 1 and 3")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")

print("You chose: " + str(RPS(player).name) + ".\n")
print("Computer chose: " + str(RPS(computer).name))

print("")

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
 