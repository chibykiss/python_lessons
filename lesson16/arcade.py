import sys
import rps
import guess_number

def arcade(name='Player'):
    first_time = False
    while True:
        # if first_time:
        #     print(f"\n{name}, Welcome to the arcade!\n\n")
        #     first_time = False
        # else:
        if first_time:
            print(f"\n{name}, Welcome back to the arcade!\n\n") 

        playerChoice = input(f"Please choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press x to exit the arcade\n")

        if playerChoice not in ["1", "2", "x"]:
                print(f"{name} please enter 1, 2, or x to exit.\n")
                return arcade()
        
        first_time = True
        
        if playerChoice == 'x':
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")
        elif playerChoice == '1':
            play = rps.rps(name)
            play()
        else:
            guess = guess_number.guess_number(name)
            guess()

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

    print(f"\n{args.name}, Welcome to the Arcade! 🐱‍🚀\n")

    play_arcade = arcade(args.name)

    play_arcade()