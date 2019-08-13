# Initiated: 7/15/19 2035 PST
# Completed: 7/23/19 2244 PST
# Updated: 8/12/19 2246 PST

# This is the game board positions which will be used to place the X's and the O's
game_board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

# This shows what the position layout is for the game moves
tic_tac_toe_positions = ("___________________________________________________________\n\n"
    "This is the layout for the moves you can make in the game\n\n"
    "1" + " | " + "2" + " | " + "3\n"
    "4" + " | " + "5" + " | " + "6\n"
    "7" + " | " + "8" + " | " + "9\n\n"
    "___________________________________________________________\n\n"
)


# This dictionary shows the user all open positions on game_board.  The index starts at 1 for the user's convenience
# I used a dictionary to make user interaction easier.  With this setup, the user does not have to begin counting
# positions from 0 (which may be confusing for some users), rather the user can start from 1, which is more intuitive
open_positions = {1: "0", 2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6", 8: "7", 9: "8"}


# This function prints out the board for the user to see which positions are open and their progress
def display_board():
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])


# This dictionary initially assigns the boolean value "False" to whether the winner is found.  In the function
# winner_decider(), once a winner has been determined, this value changes to "True".  This change signals to
# the turn_loop() to terminate
winner_found_status = {"found": False}


# This function contains all the steps for Player One's Turn.  This function takes the input and checks if that position
# is open.  If it is open, the player's token (X) is placed in that position.  If the players position is not open,
# the function loops to the beginning, prompting the player to input another position.  This function also tackles
# various errors, which are, KeyError, ValueError, and IndexError.
def player_one():
    try:
        print("\nIt is " + player_one_name + "'s turn")
        print("The following positions are open:\n", list(open_positions.keys()), "\n")
        player_turn = int(input("Enter any open position from 1 - 9\n"))
        if game_board[player_turn - 1] == "-":
            game_board[player_turn - 1] = "X"
            del open_positions[player_turn]
            print("\n\n")
            display_board()
        elif game_board[player_turn - 1] != "-":
            print("\nOops!  Looks like that isn't an open position, " + player_one_name + ".\nPlease try again\n")
            player_one()
    except KeyError:
        print("\nOops!  Looks like that isn't an open position\nPlease try again\n")
        player_one()
    except ValueError:
        print("\nOops!  Looks like that isn't a valid input\nPlease try again\n")
        player_one()
    except IndexError:
        print("\nOops!  Looks like that input is out of range\nPlease try again\n")
        player_one()


# This function is the Player Two counterpart of player_one().  If you want to read the comment from above, with two
# small changes, it is below.  Can you find the small changes?  Hint: They are regarding which player's turn it is.

# This function contains all the steps for Player Two's Turn.  This function takes the input and checks if that position
# is open.  If it is open, the player's token (O) is placed in that position.  If the players position is not open,
# the function loops to the beginning, prompting the player to input another position.  This function also tackles
# various errors, which are, KeyError, ValueError, and IndexError.
def player_two():
    try:
        print("\nIt is " + player_two_name + "'s turn")
        print("The following positions are open:\n", list(open_positions.keys()), "\n")
        player_turn = int(input("Enter any open position from 1 - 9\n"))
        if game_board[player_turn - 1] == "-":
            game_board[player_turn - 1] = "O"
            del open_positions[player_turn]
            print("\n\n")
            display_board()
        elif game_board[player_turn - 1] != "-":
            print("\nOops!  Looks like that isn't an open position, " + player_two_name + ".\nPlease try again\n")
            player_two()
    except KeyError:
        print("\nOops!  Looks like that isn't an open position\nPlease try again\n")
        player_two()
    except ValueError:
        print("\nOops!  Looks like that isn't a valid input\nPlease try again\n")
        player_two()
    except IndexError:
        print("\nOops!  Looks like that input is out of range\nPlease try again\n")
        player_two()


# This function gathers the player names and sets them as global variables
def player_name():
    global player_one_name
    player_one_name = input("\nPlayer 1 Enter your name:\n")
    global player_two_name
    player_two_name = input("\nPlayer 2 Enter your name:\n")
    return player_one_name, player_two_name


# This function prints the necessary statement for when the game ends in a tie
def tie_game():
    print("\nGreat Game!  That is a tie!")


# This function is the heart of the game.  It goes through the loop of turns and determines whether a player has won
# or if the game cannot continue (that is, it has ended in a tie).
def turn_loop():
    turns_left = 9
    while turns_left > 0:
        if not winner_found_status["found"]:
            player_one()
            winner_decider()
            turns_left = turns_left - 1
            if turns_left == 0 and not winner_found_status["found"]:
                tie_game()
            elif not winner_found_status["found"]:
                turns_left = turns_left - 1
                player_two()
                winner_decider()


# This function takes as parameters the boolean values of the two possible winners from the function winner_decider().
# Using these values, the winner (the player with the boolean value of True) is printed.
def name_winner(player_one_winner, player_two_winner):
    global player_one_name
    global player_two_name
    if player_one_winner:
        print("\nGreat Game!  " + player_one_name + " wins!\n")
    elif player_two_winner:
        print("\nGreat Game!  " + player_two_name + " wins!\n")


# This function determines whether a player has won.  It goes through all 16 possible winner scenarios (8 for each
# player: 3 rows, 3 columns, and 2 diagonals).  If a winner is found, the boolean value for the winner_found_status
# dictionary is changed to True, ending the turn_loop() function, and the name_winner function is called using the
# two parameters which show which player has won (player_one_winner and player_two_winner)
def winner_decider():
    if game_board[0] == "X" and game_board[1] == "X" and game_board[2] == "X":
        winner_found = True
        player_one_winner = True
        player_two_winner = False
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)

    elif game_board[3] == "X" and game_board[4] == "X" and game_board[5] == "X":
        winner_found = True
        player_one_winner = True
        player_two_winner = False
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[6] == "X" and game_board[7] == "X" and game_board[8] == "X":
        winner_found = True
        player_one_winner = True
        player_two_winner = False
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[0] == "X" and game_board[3] == "X" and game_board[6] == "X":
        winner_found = True
        player_one_winner = True
        player_two_winner = False
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[1] == "X" and game_board[4] == "X" and game_board[7] == "X":
        winner_found = True
        player_one_winner = True
        player_two_winner = False
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[2] == "X" and game_board[5] == "X" and game_board[8] == "X":
        winner_found = True
        player_one_winner = True
        player_two_winner = False
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[0] == "X" and game_board[4] == "X" and game_board[8] == "X":
        winner_found = True
        player_one_winner = True
        player_two_winner = False
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[2] == "X" and game_board[4] == "X" and game_board[6] == "X":
        winner_found = True
        player_one_winner = True
        player_two_winner = False
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)

    if game_board[0] == "O" and game_board[1] == "O" and game_board[2] == "O":
        winner_found = True
        player_one_winner = False
        player_two_winner = True
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[3] == "O" and game_board[4] == "O" and game_board[5] == "O":
        winner_found = True
        player_one_winner = False
        player_two_winner = True
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[6] == "O" and game_board[7] == "O" and game_board[8] == "O":
        winner_found = True
        player_one_winner = False
        player_two_winner = True
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[0] == "O" and game_board[3] == "O" and game_board[6] == "O":
        winner_found = True
        player_one_winner = False
        player_two_winner = True
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[1] == "O" and game_board[4] == "O" and game_board[7] == "O":
        winner_found = True
        player_one_winner = False
        player_two_winner = True
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[2] == "O" and game_board[5] == "O" and game_board[8] == "O":
        winner_found = True
        player_one_winner = False
        player_two_winner = True
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[0] == "O" and game_board[4] == "O" and game_board[8] == "O":
        winner_found = True
        player_one_winner = False
        player_two_winner = True
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)
    elif game_board[2] == "O" and game_board[4] == "O" and game_board[6] == "O":
        winner_found = True
        player_one_winner = False
        player_two_winner = True
        if winner_found:
            winner_found_status["found"] = True
            name_winner(player_one_winner, player_two_winner)


# This function initiates the game of Tic-Tac-Toe
def play_game():
    player_name()

    print("\n\n")

    print(tic_tac_toe_positions)

    display_board()

    turn_loop()


# Let's play!
play_game()
