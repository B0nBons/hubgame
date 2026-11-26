import random

def higher_lower():
    # the main goal for these games is going to be working on try/except statements and good error handling
    pass

def connect_four():
    def _print_grid():
        for row in grid:
            print(*row)
            # the star unpacks it (asterik but ykwim)

    def _computer_move():
        # logically this should account for player moves, add this after everything else works tho
        pass
    def _player_move():
        # ok im thinking im doing internal methods wrong so im just gonna mvoe this to a new file

    def _check_win():
        pass

    def something_important_later():
        pass

    grid = []
    for x in range(6):
        grid.append(["| X |", "| X |", "| X |", "| X |", "| X |", "| X |" ])
    _print_grid()

    # for for loop, also going to have an internal strategy method for the robot
    ongoing = True
    player_win = None
    ai_strat = None # ik its not an ai but im not typing it as "algo strat"

    # need to lock in so bad rn

    while ongoing == True:
        print("were doing connect 4")
        token = input("One character for token ")
        _print_grid()
        player_inp = int(input("What column would you like to place your token in ")) - 1
        _player_move(player_inp)
        # yay finally on player part

# i keep doomscrolling slack, PLEASE ban me
# so we ARE gonna have to make an ai play thing so thats gonna be 'fun'
# i also am doing this to learn internal methods bc the last time i did internal methods was literally four years ago

connect_four()