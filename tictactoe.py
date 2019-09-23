#!C:\Users\subodh p\AppData\Local\Programs\Python\Python37-32\python.exe



#game board
board = [ "-","-","-",
          "-","-","-",
          "-","-","-" ]

game_still_going = True

#who won or tie
winner = None

#who's turn
current_player = "X"


def display():
    print( board[0] + "|" + board[1] + "|" + board[2] )
    print( board[3] + "|" + board[4] + "|" + board[5] )
    print( board[6] + "|" + board[7] + "|" + board[8] )


def play_game():
    #display initial board

    display()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner + "won")
    elif winner == None:
        print("tie")
    
        

def handle_turn(player):

    print(player + "s turn")
    pst = input("enter a position from 1-9: ")

    valid = False
    while not valid:
    
        while pst not in ["1","2","3","4","5","6","7","8","9"]:
            pst = input(" invalid input:enter a position from 1-9: ")
      
        pst = int(pst) - 1

        if board[pst] == "-":
            valid= True
        else:
           print("cant be overwritten")
       

    board[pst] = player


    display()

def check_if_game_over():

    #check if any player has won or tie
    check_win()
    check_tie()


    
def check_win():

    global winner
     
    #check rows
    row_winner = check_row()
    #check columns
    column_winner = check_column()
    #check diagonals
    diagonal_winner = check_diagonal()
    if row_winner:
        #there was a win
        winner = row_winner

    elif column_winner:
        #there was a win
        winner = column_winner
        
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        #there was no win
        winner= None

def check_tie():
    global game_still_going
    if "-" not in board:
       game_still_going = False
       
    return

def check_row():

    global game_still_going

    r1 = board[0] == board[1] == board[2] != "-"
    r2 = board[3] == board[4] == board[5] != "-"
    r3 = board[6] == board[7] == board[8] != "-"

    if r1 or r2 or r3:
        game_still_going = False
        
    if r1:
        return board[0]

    elif r2:
        return board[3]
    elif r3:
        return board[6]
    return
    



    
def check_column():
    
    global game_still_going

    c1 = board[0] == board[3] == board[6] != "-"
    c2 = board[1] == board[4] == board[7] != "-"
    c3 = board[2] == board[5] == board[8] != "-"

    if c1 or c2 or c3:
        game_still_going = False
        
    if c1:
        return board[0]

    elif c2:
        return board[1]
    elif c3:
        return board[2]
    return
    
    return

def check_diagonal():
      
    global game_still_going

    d1 = board[0] == board[4] == board[8] != "-"
    d2 = board[2] == board[4] == board[6] != "-"
   

    if d1 or d2:
        game_still_going = False
        
    if d1:
        return board[0]

    elif d2:
        return board[2]
    
    return
    
    return




def flip_player():
    global current_player
    if current_player== "X":
        current_player ="O"
    elif current_player =="O":
        current_player = "X"
    return



    
play_game()



    

    




    

