import random
board=[] # List for our connect 4 board

# Function to generate a connect 4 board
# gen_board(list, x_coord, y_coord)
# List is an empty list element on which board is to be made
# x_coord is the number of columns in the board
# y_coord is the number of rows in the board (except the base row)

def gen_board(list,x_coord=6,y_coord=6):
    list = [["X"]*x_coord for _ in range(y_coord)] # Using "X" as the default element for every place
    base = [] # The base row
    for i in range(x_coord): # Generating the base row till the no of columns
        base.append(f"{str(i)}")
    list.append(base) # Adding the base row to the board list
    return list # Returning the list


board = gen_board(board)

# Function to display the board in the console

def display_board():
    for i in range(len(board)):
        if i==(len(board)-1):print("..............................");print(board[i]);
        else:print(board[i]) # Printing the board row by row
    print(".....................") # Just some separator for formatting

display_board()

def print_b(board):
    f=[]
    for row in board:
        e = " ".join(row)
        f.append(e)
    l="\n".join(f)
    return l

# Function to mark a element in the board
# mark_board(x_coord, player)
# x_coord is the column in which the element needs to be marked
# Player is the player whose turn is going on

def mark_board(x_coord,player=1):
    p="1" if player == 1 else "2" # 1 means player 1 and and 2 means player 22
    moved=False
    im=False
    for i in range(len(board)-1):
        if board[i][x_coord] != "X":
            if i==0:
                print("Invalid Move") # This means that there is no element left to mark in the given column
                im=True
            else:board[i-1][x_coord]=p # Marking the element
            moved=True # We marked, i.e., moved
            break
    if not moved:
       n=int(len(board))
       board[n-2][x_coord]=p
    return [check_win(player), player, im] # Check if player won by the move

def check_win(player=1):
    p="1" if player==1 else "2"
    win=False
    s_win=True
    s_win_c=0
    h_win=True
    h_win_c=0
    d_win_1=True
    d_win_1_c=0
    d_win_2=True
    d_win_2_c=0

    # Checking for a vertical win (straight win)
    for i in range(len(board)-1):
        for x in range(len(board[i])):
            if board[i][x] != "X" and board[i][x]==p:
                s_win_c=0 
                s_win=True
                try:
                    for j in range(3):
                        if i+j+1>=len(board)-1:
                            s_win=False
                            break
                        elif board[i+j+1][x]==p:
                            s_win_c+=1
                        else:
                            s_win=False
                            break
                    if s_win is True and s_win_c==3:
                        print(f"{player} won with x: {x+1} and y: {i+1} (s win)")
                        win=True
                        break                   
        
                except IndexError:
                    s_win=False
                    break
        else:continue
        break        
            #break

    # Checking for a horizontal win
    for i in range(len(board)-1):
        for x in range(len(board[i])):
            if board[i][x] != "X" and board[i][x]==p:
                h_win_c=0
                h_win=True
                try:
                    for j in range(3):
                        if x+j+1>=len(board[i]):
                            h_win=False
                            break
                        elif board[i][x+j+1]==p:
                            h_win_c+=1
                        else:
                            h_win=False
                            break
                    if h_win is True and h_win_c==3:
                        print(f"{player} won with x: {x+1} and y: {i+1} (h win)")
                        win=True
                        break                   
                except IndexError:
                    print("Index error")
                    h_win=False
                    break
        else:continue
        break

    
    # Checking for diagonal win (first)
    for i in range(len(board)-1):
        for x in range(len(board[i])):
            if board[i][x] != "X" and board[i][x]==p:
                d_win_1_c=0
                d_win_1=True
                try:
                    for j in range(3):
                        if i-j-1<0:
                            d_win_1=False
                            break                        
                        elif x+j+1>=len(board[i]):
                            d_win_1=False
                            break
                        elif board[i-j-1][x+j+1]==p:
                            d_win_1_c+=1
                        else:
                            d_win_1=False
                            break
                    if d_win_1 is True and d_win_1_c==3:
                        print(f"{player} won with x: {x+1} and y: {i+1} (d1 win)")
                        win=True
                        break                   
                except IndexError:
                    print("Index error")
                    d_win_1=False
                    break
        else:continue
        break

    # Checking for diagonal win (second)
    for i in range(len(board)-1):
        for x in range(len(board[i])):
            if board[i][x] != "X" and board[i][x]==p:
                d_win_2_c=0
                d_win_2=True
                try:
                    for j in range(3):
                        if i-j-1<0:
                            d_win_2=False
                            break                        
                        elif x-j-1>=len(board[i]):
                            d_win_2=False
                            break
                        elif board[i-j-1][x-j-1]==p:
                            d_win_2_c+=1
                        else:
                            d_win_2=False
                            break
                    if d_win_2 is True and d_win_2_c==3:
                        print(f"{player} won with x: {x+1} and y: {i+1} (d2 win)")
                        win=True
                        break                   
                except IndexError:
                    print("Index error")
                    d_win_2=False
                    break
        else:continue
        break


    return win  


p=1
while True:
    x=int(input("Enter X coordinate: "))
    if x>=len(board) or x<0:
        print("Invalid Move")
        continue
    else: won=mark_board(x, p)
    display_board()    
    if won[0] is True: 
        print(f"Player {won[1]} won so game ended")
        break

    if won[2] is False:
        p = 2 if p==1 else 1