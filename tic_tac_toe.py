import numpy as np
import pygame
import math

# Note that all constants are defined at the beginning of the code so they can be  changed easily.

rows = 3
columns = 3

width=600
height=600
size = (width, height)
white = (255, 255, 255)
black=(0,0,0)
circle=pygame.image.load("circle.png")
cross=pygame.image.load("x.png")
red=(255,0,0)
blue=(0,0,255)

# mark the position where the player clicks
def mark(row, col, player):
	board[row][col] = player

# check if the selected spot has been picked before
def is_valid_mark(row, col):
	return board[row][col] == 0


def is_board_full():
	for r in range(rows):
		for c in range(columns):
			if board[r][c] == 0:
				return False
	return True


def draw_board():
	for c in range(columns):
		for r in range(rows):
			if board[r][c] == 1:
				#the blit function places an image with the following arguments,
				#the image to be placed, the postions
				#the 50 indicates an offset to center the position of the image
				window.blit(circle, ((c*200)+50,(r*200)+50))
			elif board[r][c] ==2:
				window.blit(cross, ((c*200)+50,(r*200)+50))
		pygame.display.update()


def draw_lines():
	#This line takes the following as arguments:
	#the window we are drawing in, the color of the line, the positions, and the width of the line
	pygame.draw.line(window, black, (200,0), (200,600), 10)

	#This line draws the other vertical line 2 pixels to the right
	pygame.draw.line(window, black, (400,0), (400,600), 10)

	#The following is for horizontal lines on the window
	pygame.draw.line(window, black, (0,200), (600,200), 10)

	#This line draws the other horizontal line 2 pixels to the right
	pygame.draw.line(window, black, (0,400), (600,400), 10)


def is_winning_move(player):
	if player == 1:
		winning_color=blue
	else:
		winning_color=red
	for r in range(rows):
		if board[r][0] == player and board[r][1] == player and board[r][2] == player:
			pygame.draw.line(window, winning_color, (10, (r*200) + 100), (width-10, (r*200)+100), 10)
			return True
	for c in range(columns):
		if board[0][c] == player and board[1][c] == player and board[2][c] == player:
			pygame.draw.line(window, winning_color, ((c*200) + 100, 10), ((c*200)+100, height-10), 10)
			return True
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
			pygame.draw_line(window, winning_color, (10, 10), (590, 590), 10)
			return True
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
			pygame.draw_line(window, winning_color, (590, 10), (10, 590), 10)
			return True



board = np.zeros((rows, columns))

game_over = False

Turn = 0

#pygame is initialized
pygame.init()

#The window size is defined
window = pygame.display.set_mode(size)

#This line is used to give a title to the window
pygame.display.set_caption("tic tac toe")

#set the background of the window to white
window.fill(white)

#Draw the black lines dividing the board
draw_lines()

#This line must be used after modifying anything in the display
pygame.display.update()

pygame.time.wait(2000)

while not game_over:
	#The event codes below enables the program listen for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:

			#print the event position
			print(event.pos)

			if Turn % 2 == 0:
				#Player 1
				row = math.floor(event.pos[1]/200)
				col = math.floor(event.pos[0]/200)
				if is_valid_mark(row, col):
					mark(row, col, 1)
					if is_winning_move(1):
						game_over = True
				else:
					Turn -=1

			else:
				#Player 2
				row = math.floor(event.pos[1]/200)
				col = math.floor(event.pos[0]/200)
				if is_valid_mark(row, col):
					mark(row, col, 2)
					if is_winning_move(2):
						game_over = True
				else:
					Turn -=1
			Turn +=1
			print(board)
			draw_board()
	if is_board_full():
		game_over=True
	if game_over == True:
	 	print("Game Over")
	 	pygame.time.wait(2000)
	 	board.fill(0)
	 	window.fill(white)
	 	draw_lines()
	 	draw_board()
	 	game_over=False
	 	pygame.display.update()
