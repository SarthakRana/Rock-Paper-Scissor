import random


def start_play(best_of):
    choice_list = [1, 2, 3]
    player1_score = 0
    player2_score = 0
    try:
        for round in range(best_of):
            print("#"*128)
            print(f'Round # {round + 1}')
            valid_selection = False
            while not valid_selection:
                player1 = input(
                    "Enter your selection : (1->Rock , 2->Paper, 3->Scissor)")
                if not player1.isdigit():
                    print("Please enter a number as your selection.")
                    valid_selection = False
                else:
                    player1 = int(player1)
                    if(player1 != 1 and player1 != 2 and player1 != 3):
                        print("Invalid selection. Please select again.")
                        valid_selection = False
                    else:
                        valid_selection = True
                        player2 = random.choice(choice_list)
                        print(f'Computer selected : {player2}')
                        player1_score, player2_score = round_win(player1,
                                                                 player2,
                                                                 player1_score,
                                                                 player2_score)
        winner_player = winner(player1_score, player2_score)
        return winner_player

    except Exception as e:
        print("Exception occurred with message : ", e)


def round_win(player1, player2, player1_score, player2_score):
    if player1 == 1 and player2 == 2:
        player2_score += 1
        print("Computer wins the round !!!")
    elif player1 == 1 and player2 == 3:
        player1_score += 1
        print("Player 1 wins the round !!!")
    elif player1 == 2 and player2 == 1:
        player1_score += 1
        print("Player 1 wins the round !!!")
    elif player1 == 2 and player2 == 3:
        player2_score += 1
        print("Computer wins the round !!!")
    elif player1 == 3 and player2 == 1:
        player2_score += 1
        print("Computer wins the round !!!")
    elif player1 == 3 and player2 == 2:
        player1_score += 1
        print("Player 1 wins the round")
    elif (player1 == 1 and player2 == 1) or (player1 == 2 and player2 == 2)
    or (player1 == 3 and player2 == 3):
        print("This round is a draw !!!")
    return player1_score, player2_score


def winner(player1_score, player2_score):
    print("#"*128)
    if player1_score > player2_score:
        return "!!! PLAYER 1 WON THE GAME !!!"
    elif player1_score < player2_score:
        return "!!! COMPUTER WON THE GAME !!!"
    else:
        return '!!! GAME TIED !!!'


if __name__ == '__main__':
    try:
        play = True
        while play:
            valid_no_of_rounds = False
            while not valid_no_of_rounds:
                best_of = input(
                    "Enter the number of rounds you want to play : ")
                if not best_of.isdigit():
                    print("Please enter valid no. of rounds")
                    valid_no_of_rounds = False
                else:
                    valid_no_of_rounds = True
                    best_of = int(best_of)
                    if(best_of % 2 == 0):
                        print(
                            "Even number of rounds not allowed. "
                            "Please enter an odd number !")
                    else:
                        winner_player = start_play(best_of)
                        print(winner_player)
                        valid_play_again = False
                        while not valid_play_again:
                            play_again = input(
                                "Do you want to play another game ? (y/n)")
                            if (play_again != 'y' and play_again != 'n'):
                                print("Please select a valid option.")
                                valid_play_again = False
                            else:
                                valid_play_again = True
                                if play_again == 'y':
                                    play = True
                                    print("\nGet Ready\n")
                                else:
                                    play = False
                                    print("\nSee ya, bye!\n")
                                print("#"*128)

    except Exception as e:
        print("Exception occurred with message : ", e)
