import itertools


def win(current_game):
    def all_same(list):
        if list.count(list[0]) == len(list) and list[0] != 0:
            return True
        else:
            return False

    # HORIZONTAL
    for row in current_game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    # VERTICAL
    for col in range(len(current_game)):
        check = []

        for row in current_game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True

    # DIAGONAL
    check = []

    for i in range(len(current_game)):
        check.append(current_game[i][i])

    if all_same(check):
        print(f"Player {check[0]} is the winner diagonally (/)!")
        return True

    check = []

    for col, row in enumerate(reversed(range(len(current_game)))):
        check.append(current_game[row][col])

    if all_same(check):
        print(f"Player {check[0]} is the winner diagonally (\\)!")
        return True

    return False

# DISPLAY GAME BOARD
def display_game(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied! Try another.")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error:", e, "> Row/Column input must be 0, 1, or 2")
        return game_map, False

    except Exception as e:
        print("Error:", e, "> Something went really wrong.")
        return game_map, False


# GAME ENGINE
play = True
players = itertools.cycle([1,2])
while play:
    game_size = int(input("How big would you like your tic-tac-toe board? "))
    game = [[0 for i in range(game_size)] for j in range(game_size)]

    game_won = False
    game, _ = display_game(game, just_display=True)
    while not game_won:
        current_player = next(players)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            col_choice = int(input("What column do you want to play? (0,1,2): "))
            row_choice = int(input("What row do you want to play? (0,1,2): "))
            game, played = display_game(game, current_player, row_choice, col_choice)

        if win(game):
            game_won = True
            again = input("Would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Bye!")
                play = False
            else:
                print("Not a valid answer, so... Bye!")
                play = False
