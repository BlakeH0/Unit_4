# Player Distinction
print("Welcome to Tic-Tac-Toe! Player 1 is X's and Player 2 is O's.")
p1_name = input("Player one what is your name? ")
p2_name = input("Player two what is your name? ")

# Board
restart = False
board = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

game = True
board_spaces = 9
# if restart == True:
#     board = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#         ]

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



# print_board()

# Player Turn Function 
def player_turn(player):
    global board
    turn = input(f"{player} where would you like to place your move? ")
    if player == p1_name:
        for row in range(0, len(board)):
            for item in board[row]:
    # print_board()
                
    pass



player_turn(p1_name)
### GAME FUNCTIONALITY ###
