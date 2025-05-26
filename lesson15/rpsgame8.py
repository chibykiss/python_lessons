import sys
import random
from enum import Enum

def rps(name='Player'):

    game_count = 0
    win_count = 0
    lose_count = 0
    tie_count = 0

    def play_rps():

        nonlocal win_count, lose_count, tie_count
        nonlocal name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3


        playerchoice = input(f"\n{name}, enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"Invalid input. {name} please enter 1, 2, or 3.")
            return play_rps()
        
        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name} you chose: {str(RPS(player).name)}.")
        print(f"Computer chose: {str(RPS(computer).name)}.\n")

        def decide_winner(player, computer):
            # Use nonlocal to modify the outer function's variables
            nonlocal win_count, lose_count, tie_count, name
           
            if player == 1 and computer == 3:
                win_count += 1
                return f"🎉 {name} You win!"
            elif player == 2 and computer == 1:
                win_count += 1
                return f"🎉 {name} You win!"
            elif player == 3 and computer == 2:
                win_count += 1
                return f"🎉 {name} You win!"
            elif player == computer:
                tie_count += 1
                return "😳 It's a tie!"    
            else:
                lose_count += 1
                return "🐍 Computer wins!"
            
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n{name}, you have played {game_count} games, won {win_count}, lost {lose_count} and tied {tie_count}.\n")

        print(f"\n{name} Play again?")

        while True:
            playagain = input("\n{name} please, enter 'Y' to play again \n or 'Q' to quit:\n").lower()
            if playagain not in ['y', 'q']:
                continue
            else:
                break
        
        if playagain == 'y':
            return play_rps()
        else:
            print("\n🎉 🎉 🎉 🎉")
            print("Thanks for playing!\n")
            sys.exit(f"Bye {name}!!!")

    return play_rps



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalised game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", type=str,
        default="Player", help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)

    rock_paper_scissors()
 