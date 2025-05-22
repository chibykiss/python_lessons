def parent_function(person, coins):
    #coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(f"{person} has {coins} coins left.")
        elif coins == 1:
            print(f"{person} has {coins} coin left.")
        else:
            print(f"{person} has no coins left.")
            
    return play_game

vibe = parent_function("Vibe", 3)
vibe()
vibe()
vibe()
