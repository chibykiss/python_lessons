import sys
import random

# value = input('Please enter a value:\n')

# print(value)

print("")
playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter a number between 1 and 3")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")

print("You chose: " + playerchoice + ".\n")
print("Computer chose: " + computerchoice)

print("")

if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
elif player == computer:
    print("It's a tie!")    
else:
    print("You lose!")
 