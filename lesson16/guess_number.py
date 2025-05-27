import sys
import random
from enum import Enum

def guess_number(name='Player'):
    game_count = 0
    win_count = 0
    lose_count = 0
    win_percentage = 0.00

    def play_guess_number():
        nonlocal win_count, lose_count, game_count, win_percentage, name

        playersGuess = input(f"\n{name}, guess which number I'm tinking of... 1, 2, or 3.\n")

        if playersGuess not in ["1", "2", "3"]:
            print(f"{name} please enter 1, 2, or 3.")
            return play_guess_number()
        
        comp_choice = int(random.choice("123"))
        playersGuess = int(playersGuess)

        print(f"\n{name} you guessed: {playersGuess}.")
        print(f"I was thinking of the number: {comp_choice}.\n")

        def decide_winner(comp_choice,player_choice):
            nonlocal name, win_count, lose_count, win_percentage
            if comp_choice == player_choice:
                win_count += 1
                return f"🎉 {name} You win!"
            else:
                lose_count += 1
                return f"Sorry, {name}. Better luck next time 😢"
            
        result = decide_winner(comp_choice,playersGuess)
        print(result)

        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {win_count}")
        print(f"\n{name}'s losts: {lose_count}")

        print(f"\nYour winning percentage is: {win_count / game_count:.2%}")

        while True:
            playagain = input(f"\nPlay again, {name}? \n\n Y for yes or \n Q to quit\n").lower()
            if playagain not in ["y","q"]:
                continue
            else:
                break
        
        if playagain == 'y':
            return play_guess_number()
        else:
            print("\n🎉 🎉 🎉 🎉")
            print("Thanks for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else:
                return
          
    
    return play_guess_number

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

    guess_number_game = guess_number(args.name)

    guess_number_game()