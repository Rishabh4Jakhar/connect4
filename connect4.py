import random
board=[]
def gen_board(board,x=6,y=6):
    board = [["X"]*x for _ in range(y)]
    base = []
    for i in range(x):
        base.append(f"{str(i)}")
    board.append(base)
    return board
board = gen_board(board)
def display_board():
    for i in board:print(i)
    print(".....................")
display_board()
def print_b(board):
    f=[]
    for row in board:
        e = " ".join(row)
        f.append(e)
    l="\n".join(f)
    return l

def mark_board(x,player=1):
    p="1" if player == 1 else "2"
    moved=False
    for i in range(len(board)-1):
        if board[i][x] != "X":
            if i==0:print("Invalid Move")
            else:board[i-1][x]=p
            moved=True
            break
    if not moved:
        n=int(len(board))
        board[n-2][x]=p
    check_win(player)

def check_win(player=1):
    p="1" if player==1 else "2"
    s_win=True
    s_win_c=0
    d_win_1=True
    d_win_1=0
    d_win_2=True
    d_win_2=0
    for i in range(len(board)-1):
        for x in range(len(board[i])):
            if board[i][x] != "X" and board[i][x]==p:
                s_win_c=0
                try:
                    for j in range(3):
                        if i+j+1>=len(board)-1:
                            s_win=False
                            break
                        if board[i+j+1][x]==p:
                            s_win_c+=1
                        else:
                            s_win=False
                            break
                    if s_win is True and s_win_c==3:
                        print(f"{player} won with x: {x+1} and y: {i+1}")
                        break                   
                    break
                except IndexError:
                    s_win=False
                    break
        else:continue
        break        
            #break




y=True
while y:
    x=int(input("Enter X coordinate: "))
    if x>=len(board) or x<0:print("Invalid Move")
    else: mark_board(x, 1)
    display_board()
    yes=input("want to continue ?")
    if yes=="yes":y=False