# Player Distinction
print("Welcome to Tic-Tac-Toe! Player 1 is X's and Player 2 is O's.")
p1_name = input("Player one what is your name? ")
p2_name = input("Player two what is your name? ")

# Board
board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]

restart = False




# Print Board Function
def print_board():
    global board
    line = "---------\n"
    row_str = ""
    for row in range(0, len(board)):
        for i in range(3):
            row_str += str(board[row][i])
            if i < 2:
                row_str += " | "
            else:
                if row < 2:
                    row_str += "\n"
                    row_str += line
    print(row_str)



def print_player_wins(player):
    print(f"{player} has won this round! ")

def end_game():
    global running
    pass
    # Check Horizontal Win
    x_score = 0
    o_score = 0
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == "X":
                print_board()
                print_player_wins(p1_name)
                return True
            else:
                print_board()
                print_player_wins(p2_name)
                return True

                

    # Check Vertical Win
    if board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] == "X":
            print_board()
            print_player_wins(p1_name)
            return True
        else:
            print_board()
            print_player_wins(p2_name)
            return True 
    elif board[0][1] == board[1][1] == board[2][1]:
        if board[0][0] == "X":
            print_board()
            print_player_wins(p1_name)
            return True
        else:
            print_board()
            print_player_wins(p2_name)
            return True 
    elif board[0][2] == board[1][2] == board[2][2]:
        if board[0][0] == "X":
            print_board()
            print_player_wins(p1_name)
            return True
        else:
            print_board()
            print_player_wins(p2_name)
            return True 



    # Check Diagonal Win
    if board[0][0] == board [1][1] == board[2][2]:
        if board[0][0] == "X":
            print_board()
            print_player_wins(p1_name)
            return True
        else:
            print_board()
            print_player_wins(p2_name)
            return True
    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            print_board()
            print_player_wins(p1_name)
            return True
        else:
            print_board()
            print_player_wins(p2_name)
            return True


    # Check For Board
    
    for row in board:
        for item in row:
            if isinstance(item, int):
                return False

    return True



#Error Message Function
def print_error():
    print("Choose a valid/unused spot!")

# print_board()

# Player Turn Function 
def player_turn(player):
    global board
    global current_player
    print_board()
    turn = int(input(f"{player} where would you like to place your move? "))
    while True:
        print()
        valid_choice = False
        if player == p1_name:
            for item in board:
                for i in range(3):
                    if item[i] == turn:
                        item[i] = "X"
                        current_player = p2_name
                        valid_choice = True
            if valid_choice == False:
                return print_error()
            else:
                break
        elif player == p2_name:
            for elem in board:
                for x in range(3):
                    if elem[x] == turn:
                        elem[x] = "O"
                        current_player = p1_name
                        valid_choice = True
            if valid_choice == False:
                return print_error()
            else:
                break

                

current_player = p1_name

running = True
### GAME FUNCTIONALITY ###
while running:
    # Restart
    if restart == True:
        board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
        restart = False
        current_player = p1_name



    player_turn(current_player)

    # Check Win
    if end_game():
        while True:
            replay_input = input("Would you like to play again? (y/n) ")
            if replay_input == "y":
                print("Playing again... ")
                restart = True
                break
            elif replay_input == "n":
                print("See ya later! ")
                running = False
                break