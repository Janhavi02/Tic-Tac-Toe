#Global variables
board=[" "]*10
game_state=True
announce=''


#This will ignore the zero index
def reset_board():
    global game_state,board
    board= [" "]*10
    game_state=True

def display_board():
   # print("                              ")
    print " "+board[7]+"|"+board[8]+"|"+board[9]+" "
    print"--------"
    print " "+board[4]+"|"+board[5]+"|"+board[6]+" "
    print"--------"
    print " "+board[1]+"|"+board[2]+"|"+board[3]+" "
    print('\n')

def win_check(board,player):
    if( board[7] == board[8] == board[9] == player) or \
      ( board[4] == board[5] == board[6] == player) or \
      ( board[1] == board[2] == board[3] == player) or \
      ( board[7] == board[4] == board[1] == player) or \
      ( board[8] == board[5] == board[2] == player) or \
      ( board[9] == board[6] == board[3] == player) or \
      ( board[1] == board[5] == board[9] == player) or \
      ( board[7] == board[5] == board[3] == player): 
      return True
    else:
        return False

def full_board_check(board):
    #in case of tie,check any empty space in board
    if " " in board[1:]:
        return False
    else:
        return True

def ask_player(mark):
    global board
    req="Choose where to keep your : "+ mark 
    while True :
        try:
            print('\n')
            choice= int(raw_input(req))
        except ValueError:
            print("Enter number between 1-9")
            continue

        if board[choice]==" ":
            board[choice] = mark
            break
        else:
            print("THat place isn't empty")
            continue

def player_choice(mark):
    global board, game_state,announce
    announce=''
    #get player i/p
    mark=str(mark)
    #place input at correct position
    ask_player(mark)

    if win_check(board,mark):
        display_board()
        announce = mark + " wins! congratulations "
        game_state=False

    #Show board
    print('\n'*100)
    display_board()

    #in case of tie
    if full_board_check(board):
        announce = " TIE!"
        game_state = False

    return game_state,announce


def play_game():
    reset_board()
    global announce

#SET MARKS
    X='X'
    O='O'

    while True:  
        print('\n'*100)                         
        display_board()
    
         #player X turn
        game_state,announce=player_choice(X)
        print announce
        if game_state==False:
            break

        #player O turn
        game_state,announce=player_choice(O)
        print announce
        if game_state==False:
            break

    #ASk for a rematch
    rematch = raw_input("Do you want to play again? y/n ")
    if rematch=='y':
        play_game()
    else :
        print"Thank you for Playing!"

play_game()