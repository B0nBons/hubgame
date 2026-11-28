def print_grid(grid):
    for row in grid:
        print(*row)
        # the star unpacks it (asterik but ykwim)

def computer_move():
    # logically this should account for player moves, add this after everything else works tho
    pass
def player_move(col_drop, token, grid):
    strin = "| " + token + " |"
    # ok im thinking im doing internal methods wrong so im just gonna mvoe this to a new file
    for x in range(len(grid) - 1, -1, -1):
        if grid[x][col_drop] == "|   |":
            grid[x][col_drop] = strin 
            return

def check_win(grid):
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            checkme = grid[row][column]
            if checkme == "|   |":
                continue # another rare cont reference
            
            if column + 3 < len(grid[0]):
                if checkme == grid[row][column + 1] and checkme == grid[row][column + 2] and checkme == grid[row][column + 3]:
                    return True
            # checks for VERTICAL BINGO (connect??? idfk man)

            if row + 3 < len(grid):
                if checkme == grid[row + 1][column] and spot == grid[row + 2][column] and spot == grid[row + 3][column]:
                    return True

            

def something_important_later():
    pass

def mainloop():
    grid = []
    for x in range(6):
        grid.append(["|   |", "|   |", "|   |", "|   |", "|   |", "|   |" ])
    print_grid(grid)

    # for for loop, also going to have an internal strategy method for the robot
    ongoing = True
    player_win = None
    ai_strat = None # ik its not an ai but im not typing it as "algo strat"

    # need to lock in so bad rn

    while ongoing == True:
        print("were doing connect 4")
        token = input("One character for token ")
        while True:
            print_grid(grid)
            player_inp = int(input("What column would you like to place your token in ")) - 1
            player_move(player_inp, token, grid)
    
mainloop()