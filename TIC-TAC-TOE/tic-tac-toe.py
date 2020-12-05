import pygame,sys
import numpy 

pygame.init()

WIDTH=600
HEIGHT=600
BG_COLOR=(0,0,0)
LINE_COLOR=(0,228,235)
SQUARE_SIZE=200
LINE_WIDTH=15
BOARD_ROW=3
BOARD_COL=3
CROSS_COLOR=(242,242,242)
CIRCLE_COLOR=(242,242,242)
CROSS_WIDTH=25


screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BG_COLOR)
#title and icon
title=pygame.display.set_caption('TIC-TAC-TOE')
icon=pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)

#vertical and horizontal lines
def draw_lines():
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200),5)
    pygame.draw.line(screen,LINE_COLOR,(0,400),(600,400),5)
    pygame.draw.line(screen,LINE_COLOR,(200,0),(200,600),5)
    pygame.draw.line(screen,LINE_COLOR,(400,0),(400,600),5)


def draw_symbol():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if board[row][col]==1:
                pygame.draw.circle(screen,CIRCLE_COLOR,(int(col*200+100),int(row*200+100)),60,15)
            elif board[row][col]==2:
                pygame.draw.line(screen,CROSS_COLOR,(int(col*200+55),int(row*200+200-55)),(int(col*200+200-55),int(row*200+55)),CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(int(col*200+55),int(row*200+55)),(int(col*200+200-55),int(row*200+200-55)),CROSS_WIDTH)

#numpy
board=numpy.zeros((BOARD_ROW,BOARD_COL))


#marking the square
def mark_square(row,col,player):
    board[row][col]=player

#available square
def available_square(row,col):
    return board[row][col]==0

#is square full
def square_full():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if board[row][col]==0:
                return False
            
    return True

def game_win(player):
    #vertical win
    for col in range(BOARD_COL):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            vertical_line(col,player)
            return True
    #horizontal win
    for row in range(BOARD_ROW):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            horizontal_line(row,player)
            return True
    #diagonal wins
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        backslash_line(player)
        return True
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        frontslash_line(player)
        return True

    return False



def vertical_line(col,player):
    posX=col*SQUARE_SIZE+SQUARE_SIZE//2
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR

    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),15)

def horizontal_line(row,player):
    posY=row*200+100
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR

    pygame.draw.line(screen,color,(15,posY),(WIDTH-15,posY),15)



def backslash_line(player):
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR


    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),15)

def frontslash_line(player):
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR

    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),15)

    
        
#reset
def reset():
    screen.fill(BG_COLOR)
    draw_lines()
    player=1
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            board[row][col]==0
    GAMEOVER=False
            
#gameloop
player=1
GAMEOVER=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
   

        if event.type==pygame.MOUSEBUTTONDOWN and not GAMEOVER:
            mouseX=event.pos[0]
            mouseY=event.pos[1]

            #clicked
            clicked_row=int(mouseY//200)
            clicked_col=int(mouseX//200)
            if available_square(clicked_row,clicked_col):
                mark_square(clicked_row,clicked_col,player)
                if game_win(player):
                    GAMEOVER=True
                player=player%2+1
                

                draw_symbol()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                reset()


    draw_lines()
    pygame.display.update()

        
