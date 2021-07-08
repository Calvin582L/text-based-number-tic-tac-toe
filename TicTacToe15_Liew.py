# Name: Calvin Liew
# Date: 2021-01-29
# Purpose: Video game final project, Tic-Tac-Toe 15 by Calvin Liew.

import random


# Function that reminds the users of the game rules and other instructions.

def intro():
    print("""\n#######                #######                     #######                    #   ####### 
   #    #  ####           #      ##    ####           #     ####  ######     ##   #       
   #    # #    #          #     #  #  #    #          #    #    # #         # #   #       
   #    # #      #####    #    #    # #      #####    #    #    # #####       #   ######  
   #    # #               #    ###### #               #    #    # #           #         # 
   #    # #    #          #    #    # #    #          #    #    # #           #   #     # 
   #    #  ####           #    #    #  ####           #     ####  ######    #####  #####   

How to play Tic-Tac-Toe 15:           

To win, you must get three numbers in a row/column/diagonal that add up to the sum of 15! The first player enters odd numbers and the second player enters even numbers. 

Board Instructions: Tell the program the position of which you would like to enter by entering the number position of 
the boxes as shown below. Players can can only enter from numbers from 1-9. 

             |     |
	  1  |  2  |  3
	_____|_____|_____
	     |     |
	  4  |  5  |  6
	_____|_____|_____
	     |     |
	  7  |  8  |  9
	     |     |
                       """)


# Function that prints the tic-tac-toe board.

def print_board(board):
    print("\n\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("\t     |     |")


# Function that chooses who goes first and assigns the player order.

def choose_who_first(player1, player2, player_order):
    flip = random.randint(1, 2)

    if flip == 1:
        print("\n" + player1, "goes first.", player1, "can only play odd numbers and", player2,
              "can only play even numbers from 1-9. ")
        print()
        player_order.append(player1)
        player_order.append(player2)
        return player1

    elif flip == 2:
        print("\n" + player2, "goes first.", player2, "can only play odd numbers and", name1,
              "can only play even numbers from 1-9. ")
        print()
        player_order.append(player2)
        player_order.append(player1)
        return player2


# Function that calls the print_board() function as well as makes the moves that the players provide while checking if the moves are legal or not.

def make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order):
    odd_moves = [1, 3, 5, 7, 9]
    even_moves = [2, 4, 6, 8]

    try:
        if turn == player1:

            print("\nIts your turn", player1 + ": ")
            print()
            p1_move_input = int(input("Move to which space? (1-9): "))

            if player_order[0] == player1:
                if 1 <= p1_move_input <= 9 and the_board[p1_move_input - 1] == 0:
                    print()
                    p1_num_input = int(input("Enter an ODD NUMBER from 1-9: "))

                    if p1_num_input in odd_moves and p1_num_input not in unavailable_moves_p1:
                        the_board[p1_move_input - 1] = p1_num_input
                        unavailable_moves_p1.append(p1_num_input)
                    elif p1_num_input in unavailable_moves_p1:
                        print("\nINVALID INPUT, Please try again and enter a number that you haven't used. ")
                        make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
                    else:
                        print("\nINVALID INPUT, Please try again and enter an ODD number. ")
                        make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
                elif p1_move_input < 1 or p1_move_input > 9:
                    print("\nINVALID INPUT, Please try again and enter a number between 1-9. ")
                    make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
                else:
                    print("\nINVALID INPUT, Please try again and enter an unoccupied spot. ")
                    make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)

            elif player_order[1] == player1:
                if 1 <= p1_move_input <= 9 and the_board[p1_move_input - 1] == 0:
                    print()
                    p1_num_input = int(input("Enter a EVEN NUMBER from 1-9: "))

                    if p1_num_input in even_moves and p1_num_input not in unavailable_moves_p1:
                        the_board[p1_move_input - 1] = p1_num_input
                        unavailable_moves_p1.append(p1_num_input)
                    elif p1_num_input in unavailable_moves_p1:
                        print("\nINVALID INPUT, Please try again and enter a number that you haven't used. ")
                        make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
                    else:
                        print("\nINVALID INPUT, Please try again and enter a EVEN number. ")
                        make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
                elif p1_move_input < 1 or p1_move_input > 9:
                    print("\nINVALID INPUT, Please try again and enter a number between 1-9. ")
                    make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
                else:
                    print("\nINVALID INPUT, Please try again and enter an unoccupied spot. ")
                    make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)

        if turn == player2:

            print("\nIts your turn", player2 + ": ")
            print()
            p2_move_input = int(input("Move to which space? (1-9): "))

            if player_order[0] == player2:
                if 1 <= p2_move_input <= 9 and the_board[p2_move_input - 1] == 0:
                    print()
                    p2_num_input = int(input("Enter an ODD NUMBER from 1-9: "))

                    if p2_num_input in odd_moves and p2_num_input not in unavailable_moves_p2:
                        the_board[p2_move_input - 1] = p2_num_input
                        unavailable_moves_p2.append(p2_num_input)
                    elif p2_num_input in unavailable_moves_p2:
                        print("\nINVALID INPUT, Please try again and enter a number that you haven't used. ")
                        make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
                    else:
                        print("\nINVALID INPUT, Please try again and enter an ODD number. ")
                        make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
                elif p2_move_input < 1 or p2_move_input > 9:
                    print("\nINVALID INPUT, Please try again and enter a number between 1-9. ")
                    make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
                else:
                    print("\nINVALID INPUT, Please try again and enter an unoccupied spot. ")
                    make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)

            elif player_order[1] == player2:
                if 1 <= p2_move_input <= 9 and the_board[p2_move_input - 1] == 0:
                    print()
                    p2_num_input = int(input("Enter a EVEN NUMBER from 1-9: "))

                    if p2_num_input in even_moves and p2_num_input not in unavailable_moves_p2:
                        the_board[p2_move_input - 1] = p2_num_input
                        unavailable_moves_p2.append(p2_num_input)
                    elif p2_num_input in unavailable_moves_p2:
                        print("\nINVALID INPUT, Please try again and enter a number that you haven't used. ")
                        make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
                    else:
                        print("\nINVALID INPUT, Please try again and enter a EVEN number. ")
                        make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
                elif p2_move_input < 1 or p2_move_input > 9:
                    print("\nINVALID INPUT, Please try again and enter a number between 1-9. ")
                    make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
                else:
                    print("\nINVALID, Please try again and enter an unoccupied spot. ")
                    make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)

    except ValueError:
        print("\nINVALID INPUT, Please try again and enter only in integers. ")
        make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)


# Function that checks if any three numbers in a row/column/diagonal add up to 15. If there is, the function returns is_game_over and the game ends.

def check_game(board, winner):
    is_game_over = ""

    if board[0] + board[1] + board[2] == 15 and board[0] != 0 and board[1] != 0 and board[2] != 0:
        print_board(board)
        print("\n"+str(board[0])+",", str(board[1])+",", "and", str(board[2]), "add up to 15! ")
        print("\n"+winner, "wins! ")
        is_game_over = True
    elif board[3] + board[4] + board[5] == 15 and board[3] != 0 and board[4] != 0 and board[5] != 0:
        print_board(board)
        print("\n"+str(board[3])+",", str(board[4])+",", "and", str(board[5]), "add up to 15! ")
        print("\n"+winner, "wins! ")
        is_game_over = True
    elif board[6] + board[7] + board[8] == 15 and board[6] != 0 and board[7] != 0 and board[8] != 0:
        print_board(board)
        print("\n"+str(board[6])+",", str(board[7])+",", "and", str(board[8]), "add up to 15! ")
        print("\n"+winner, "wins! ")
        is_game_over = True
    elif board[0] + board[3] + board[6] == 15 and board[0] != 0 and board[3] != 0 and board[6] != 0:
        print_board(board)
        print("\n"+str(board[0])+",", str(board[3])+",", "and", str(board[6]), "add up to 15! ")
        print("\n"+winner, "wins! ")
        is_game_over = True
    elif board[1] + board[4] + board[7] == 15 and board[1] != 0 and board[4] != 0 and board[7] != 0:
        print_board(board)
        print("\n"+str(board[1])+",", str(board[4])+",", "and", str(board[7]), "add up to 15! ")
        print("\n"+winner, "wins! ")
        is_game_over = True
    elif board[2] + board[5] + board[8] == 15 and board[2] != 0 and board[5] != 0 and board[8] != 0:
        print_board(board)
        print("\n"+str(board[2])+",", str(board[5])+",", "and", str(board[8]), "add up to 15! ")
        print("\n"+winner, "wins! ")
        is_game_over = True
    elif board[6] + board[4] + board[2] == 15 and board[6] != 0 and board[4] != 0 and board[2] != 0:
        print_board(board)
        print("\n"+str(board[6])+",", str(board[4])+",", "and", str(board[2]), "add up to 15! ")
        print("\n"+winner, "wins! ")
        is_game_over = True
    elif board[0] + board[4] + board[8] == 15 and board[0] != 0 and board[4] != 0 and board[8] != 0:
        print_board(board)
        print("\n"+str(board[0])+",", str(board[4])+",", "and", str(board[8]), "add up to 15! ")
        print("\n"+winner, "wins! ")
        is_game_over = True

    return is_game_over


# Function that prints the scoreboard and the scores of the two players. Prints after a round has ended.

def score(score1, score2, player1, player2):
    print("\n\t------------------")
    print("\t    SCOREBOARD")
    print("\t------------------")
    print("\t" + "    " + player1 + ":", score1)
    print("\t" + "    " + player2 + ":", score2)
    print("\t------------------")
    print()


# Function that is where most of the game takes place. Function calls other functions such as make_move_and_update, choose_who_first, score and other code that make up the game.
# Function keeps track of the player order, the board, unavailable moves, amount of rounds and other variables. The game ends in a draw when count reaches 9. At the end of the round, it asks the users if they want to play again.

def play_game(score1, score2, player1, player2):
    unavailable_moves_p1 = []
    unavailable_moves_p2 = []
    player_order = []
    the_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = 0
    restart = ""

    turn = choose_who_first(player1, player2, player_order)

    input("Enter anything to start the round: ")

    for i in range(10):

        print_board(the_board)
        make_move_and_update(the_board, turn, player1, player2, unavailable_moves_p1, unavailable_moves_p2, player_order)
        count += 1

        if check_game(the_board, turn):
            if turn == player1:
                score1 += 1
            elif turn == player2:
                score2 += 1
            break

        if count == 9:
            print("No numbers added up to 15, it's a DRAW! ")
            break

        if turn == player1:
            turn = player2
        else:
            turn = player1

    input("\nEnter anything to continue: ")
    score(score1, score2, player1, player2)

# Asks if the players want to restart. If yes, it calls the play_game function. If no, it ends the game and congratulates the overall winner.

    while restart != "yes" or restart != "y" or restart != "n" or restart != "no":
        restart = input("Do want to play Again? (y/n) ").lower()
        if restart == "y" or restart == "yes":
            print("\nLoading new round...")
            play_game(score1, score2, player1, player2)
        elif restart == "n" or restart == "no":
            if score1 > score2:
                print("\n"+player1, "is the overall winner! Congratulations!")
            elif score2 > score1:
                print("\n"+player2, "is the overall winner! Congratulations!")
            elif score1 == score2:
                print("\nBoth players have one the same amount of rounds. It's a draw! ")
            print("\nThanks for playing! ")
            break
        else:
            print("\nPlease enter YES or NO ")
            print()


# This code manages the important things before the actual game starts such as the instructions, usernames, etc. Calls the play_game function.

if __name__ == "__main__":
    intro()

    input("Enter anything to continue: ")

    print("\nEnter usernames: ")
    name1 = input("\nPlayer 1, Enter your name: ").title()
    name2 = input("\nPlayer 2, Enter your name: ").title()

    p1_score = 0
    p2_score = 0
    play_game(p1_score, p2_score, name1, name2)
