import itertools

game = [[0,0,0], [0,0,0], [0,0,0]]


def win(current_game):
    # Horizontal
    for row in current_game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally!")

    # Vertical
    for col in range(len(current_game)):
        check = []

        for row in current_game:
            check.append(row[col])

        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically!")

    # Diagonal
    check = []

    for i in range(len(current_game)):
        check.append(current_game[i][i])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print(f"Player {check[0]} is the winner diagonally (/)!")

    check = []

    for col, row in enumerate(reversed(range(len(current_game)))):
        check.append(current_game[row][col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print(f"Player {check[0]} is the winner diagonally (\\)!")


def display_game(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error:", e, ">Row/Column input must be 0, 1, or 2")




play = True
players = itertools.cycle([1,2])
while play:
    game = [[0,0,0], [0,0,0], [0,0,0]]

    game_won = False
    game = display_game(game, just_display=True)
    while not game_won:
        current_player = next(players)
        print(f"Current Player: {current_player}")

        col_choice = int(input("What column do you want to play? (0,1,2): "))
        row_choice = int(input("What row do you want to play? (0,1,2): "))

        game = display_game(game, current_player, row_choice, col_choice)

# game = display_game(game, just_display=True)
# game = display_game(game, player = 1, row = 2, column = 1)
