import numpy as np
import pygame
import sys
import math

# Defining colors
GREEN_BORDER = (70,193,138)
GREEN = (100, 255, 184)
RED_BORDER = (146,46,32)
RED = (255, 68, 42)
YELLOW_BORDER = (199, 189, 0)
YELLOW = (234, 224, 24)
BLACK = (0,0,0)
GREY_BORDER = (120,120,120)
GREY = (69,70,69)
# Defining size of the connect 4 board
ROW_COUNT = 6
COLUMN_COUNT = 7
# Music File list
music_files = [r"assets\music\NCS bg music.wav",r"assets\music\win 1.wav", r"assets\music\click.wav"]
# Creates a matrice of 0's to be used as the connect 4 board
def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board
# Marking a move in the matrice
def drop_piece(board, row, col, piece):
	board[row][col] = piece

# Checking if the move is valid
def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0
# Return the next valid row in the column
def get_next_open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r
# Printing the board on console for reference
def print_board(board):
	print(np.flip(board, 0))
# Checking for win
def winning_move(board, piece):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True, 0,(r,c, piece)

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True, 1, (r,c, piece)

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True, 2, (r,c, piece)

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True, 3, (r,c, piece)
	
	# Check if all the places are filled
	if np.all(board != 0):
		return True, -1, (-1,-1,-1)

	return False, -1, (-1,-1,-1)



def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, GREY, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, GREY_BORDER, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
			pygame.draw.circle(screen, GREY, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS-10)
			
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, GREEN_BORDER,(int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
				pygame.draw.circle(screen, GREEN,(int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS-10)
			elif board[r][c] == 2:
				pygame.draw.circle(screen, RED_BORDER,(int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS-10)		
			elif board[r][c] == 31:
				pygame.draw.circle(screen, YELLOW,(int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS, width=10)
				pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS-10)					
			elif board[r][c] == 32:
				pygame.draw.circle(screen, YELLOW,(int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS, width=10)
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS-10)					

	pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0
pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Connect 4 - By Rishabh')
draw_board(board)
pygame.display.update()
pygame.mixer.music.load(music_files[0])
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.6)
myfont = pygame.font.SysFont("comic sans", 75)

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == 0:
				#screen.blit(p1, [posx, int(SQUARESIZE/2)])
				pygame.draw.circle(screen, GREEN_BORDER, (posx, int(SQUARESIZE/2)), RADIUS)
				pygame.draw.circle(screen, GREEN, (posx, int(SQUARESIZE/2)), RADIUS-10)
			else:
				pygame.draw.circle(screen, RED_BORDER, (posx, int(SQUARESIZE/2)), RADIUS)
				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS-10)
				#pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			#print(event.pos)
			# Ask for Player 1 Input
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 1)
					win_check = winning_move(board, 1)
					r,c=win_check[2][0], win_check[2][1]
					j=win_check[2][2]
					if win_check[0]:
						draw = False
						for i in range(4):
							if win_check[1]==0:
								board[r][c+i]=30+j
							elif win_check[1]==1:
								board[r+i][c]=30+j
							elif win_check[1]==2:
								board[r+i][c+i]=30+j
							elif win_check[1]==3:
								board[r-i][c+i]=30+j
							else:
								draw = True

						
						pygame.mixer.music.stop()
						pygame.mixer.music.unload()
						pygame.mixer.music.load(music_files[1])
						pygame.mixer.music.play()
						if draw:
							label = myfont.render("Draw!!", 0, (255,255,255))
							screen.blit(label, (40,10))
						else:
							label = myfont.render("Player 1 wins!!", 0, (100,255,184))
							screen.blit(label, (40,10))
						game_over = True


			# # Ask for Player 2 Input
			else:				
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 2)
					win_check = winning_move(board, 2)
					r,c=win_check[2][0], win_check[2][1]
					j=win_check[2][2]
					if win_check[0]:
						draw = False
						for i in range(4):
							if win_check[1]==0:
								board[r][c+i]=30+j
							elif win_check[1]==1:
								board[r+i][c]=30+j
							elif win_check[1]==2:
								board[r+i][c+i]=30+j
							elif win_check[1]==3:
								board[r-i][c+i]=30+j
							else:
								draw = True
						pygame.mixer.music.stop()
						pygame.mixer.music.unload()
						pygame.mixer.music.load(music_files[1])
						pygame.mixer.music.play()
						if draw:
							label = myfont.render("Draw!!", 0, (255,255,255))
							screen.blit(label, (40,10))
						else:
							label = myfont.render("Player 2 wins!!", 0, (255,68,42))
							screen.blit(label, (40,10))
						game_over = True
			pygame.mixer.Channel(1).play(pygame.mixer.Sound(music_files[2]))
			#pygame.mixer.Channel(2).play(pygame.mixer.Sound(music_files[0]))
			print_board(board)
			draw_board(board)

			turn += 1
			turn = turn % 2

			if game_over:
				pygame.time.wait(6000)