import pygame
import random
import sys
import time
from pygame import mixer

pygame.init()
mixer.init()
bg = mixer.Sound(r'C:/Users/M0u1ea5/Desktop/Copter/background.mp3')
point = mixer.Sound(r'C:/Users/M0u1ea5/Desktop/Copter/point.wav')
explosion = mixer.Sound(r'C:/Users/M0u1ea5/Desktop/Copter/explosion.wav')
bg.play(-1)

Screen = pygame.display.set_mode((1100,625))

backgroudImage = pygame.image.load(r'C:/Users/M0u1ea5/Desktop/Copter/city.jpg')

copterImage  = pygame.image.load(r'C:/Users/M0u1ea5/Desktop/Copter/helicopter.png')
copterX = 150
copterY = 300
copterYChange = 0

yaxis = 2

def displayCopter(x,y):
	Screen.blit(copterImage,(x,y)) 

obstacleWidth = 70
obstacleHeight = random.randint(150,400)
obstacleColor = (211,253,117)
obstacleXChange = -2.5
obstacleX = 1160


timeChanger = 0

def displayObstacle(obstacleY,height):
	pygame.draw.rect(Screen,obstacleColor,(obstacleX,obstacleY,obstacleWidth,height))

def collision(obstacleX,obstacleY,copterX,copterY,obstacleHeight):
	if copterY >= obstacleY and copterY <= (obstacleY+obstacleHeight):
		if copterX >= obstacleX-67 and copterX <= obstacleX+90:
			return True
	return False

score = 0
scorefont = pygame.font.Font('freesansbold.ttf',32)

def scoreDisplay(score):
	display = scorefont.render(f"Score: {score}",True,(255,255,255))
	Screen.blit(display,(10,10))


startfont = pygame.font.Font('freesansbold.ttf',32)
def start():
	display = startfont.render(f"Click left mouse button to START",True,(255,255,255))
	Screen.blit(display,(300,100))
	pygame.display.update()

scorelist = [0]

gm1 = pygame.font.Font('freesansbold.ttf',64) 
gm2 = pygame.font.Font('freesansbold.ttf',32)
def gameOver():
	maximum = max(scorelist)

	display1 = gm1.render(f"GAME OVER",True,(200,35,35))
	Screen.blit(display1,(360,300))

	display2 = gm2.render(f"SCORE: {score} ",True,(255,255,255))
	Screen.blit(display2,(310,400))

	display3 = gm2.render(f"HIGH SCORE: {maximum}",True,(255,255,255))
	Screen.blit(display3,(550,400))


running = True
waiting = True
Collision = False

while running:
	
	Screen.fill((0,0,0))
	
	Screen.blit(backgroudImage,(0,0))

	while waiting:
		if Collision:
			gameOver()
			start()
		else:
			start()

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					score = 0
					copterY = 300
					obstacleX = 1160
					obstacleY = random.randint(100,500)
					waiting = False

			if event.type == pygame.QUIT:
				waiting = False
				running = False


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				copterYChange = -yaxis

		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				copterYChange = yaxis

	copterY += copterYChange

	if copterY <= 50:
		copterY = 50
	if copterY >= 550:
		copterY = 550

	if timeChanger == 10:
		obstacleXChange -= 0.5
		yaxis += 0.3
		timeChanger = 0

	obstacleX += obstacleXChange
	if obstacleX <= -10:
		obstacleX = 1160
		obstacleHeight = random.randint(300,400)
		point.play(0)
		timeChanger += 1
		obstacleY = random.randint(0,300)
		score += 10

	Collision = collision(obstacleX,obstacleY,copterX,copterY,obstacleHeight)
	
	if Collision:
		scorelist.append(score)
		explosion.play(0)
		time.sleep(2)
		waiting = True

	displayObstacle(obstacleY,obstacleHeight)
	displayCopter(copterX,copterY)
	scoreDisplay(score)
	
	pygame.display.update()

pygame.quit() 