import pygame,sys
import random
import math
from tkinter import messagebox

pygame.init()

screen = pygame.display.set_mode((600,700))

#title
pygame.display.set_caption('cross the road')

#bg
bg=pygame.image.load('C:/Users/M0u1ea5/Documents/PROJECTS/cross_it/bg.png')

#baby
player_img = pygame.image.load('C:/Users/M0u1ea5/Documents/PROJECTS/cross_it/baby-boy.png')
playerX = 300
playerY = 50
playerXchange = 0
playerYchange = 0

#motorcycle
bike_img = pygame.image.load('C:/Users/M0u1ea5/Documents/PROJECTS/cross_it/motorbike.png')
bikeX = 536
bikeY = 120
bikeXchange = 0.3

#bus
chopper_img = pygame.image.load('C:/Users/M0u1ea5/Documents/PROJECTS/cross_it/chopper.png')
chopperX = 536
chopperY = 250
chopperXchange = 0.3

#police
police_img = pygame.image.load('C:/Users/M0u1ea5/Documents/PROJECTS/cross_it/police-car.png')
policeX = 536
policeY = 400
policeXchange = 0.3

#bank truck
btruck_img = pygame.image.load('C:/Users/M0u1ea5/Documents/PROJECTS/cross_it/bank-truck.png')
btruckX = 0
btruckY = 530
btruckXchange = 0

#pit_1
pit_img = pygame.image.load('C:/Users/M0u1ea5/Documents/PROJECTS/cross_it/black-hole.png')
pitX = 350
pitY = 350 

#pit 2
pit2_img = pygame.image.load('C:/Users/M0u1ea5/Documents/PROJECTS/cross_it/black-hole.png')
pit2X = 200
pit2Y = 500

#thief
thief_img = pygame.image.load('C:/Users/M0u1ea5/Documents/PROJECTS/cross_it/thief.png')
thiefX = 200
thiefY = 350
thiefXchange=0

#parents
parents_img = pygame.image.load('C:/Users/M0u1ea5/Documents/PROJECTS/cross_it/family.png')
parentX = 280
parentY = 630


#intializing images in screen 
def parent():
    screen.blit(parents_img,(parentX,parentY))

def thief(x,y):
    screen.blit(thief_img,(x,y))

def player(x,y):
    screen.blit(player_img,(x,y))

def bike(x,y):
    screen.blit(bike_img,(x,y))

def chopper(x,y):
    screen.blit(chopper_img,(x,y))

def police(x,y):
    screen.blit(police_img,(x,y))

def banktruck(x,y):
    screen.blit(btruck_img,(x,y))

def pit(x,y):
    screen.blit(pit_img,(x,y)) 

def pit2(x,y):
    screen.blit(pit_img,(x,y)) 


#collisions

def bikecollision(playerX,playerY,bikeX,bikeY):
    bike_dis=math.sqrt(math.pow(bikeX-playerX,2)+ math.pow(bikeY-playerY,2))
    if bike_dis < 35:return True
    return False

def choppercollision(playerX,playerY,busX,busY):
    chopper_dis=math.sqrt(math.pow(chopperX-playerX,2)+ math.pow(chopperY-playerY,2))
    if chopper_dis < 35:return True
    return False

def policecollision(playerX,playerY,policeX,policeY):  
    police_dis=math.sqrt(math.pow(policeX-playerX,2)+ math.pow(policeY-playerY,2))
    if police_dis < 35:return True
    return False

def banktruckcollision(playerX,playerY,btruckX,btruckY):    
    btruck_dis=math.sqrt(math.pow(btruckX-playerX,2)+ math.pow(btruckY-playerY,2))
    if btruck_dis < 35:return True
    return False

def pitcollision(playerX,playerY,pitX,pitY):
    pit_dis=math.sqrt(math.pow(pitX-playerX,2) + math.pow(pitY-playerY,2))
    if pit_dis < 50:return True
    return False

def pit2collision(playerX,playerY,pit2X,pit2Y):
    pit2_dis=math.sqrt(math.pow(pit2X-playerX,2) + math.pow(pit2Y-playerY,2))
    if pit2_dis < 50:return True
    return False

def thiefcollision(playerX,playerY,thiefX,thiefY):
    thief_dis=math.sqrt(math.pow(thiefX-playerX,2) + math.pow(thiefY-playerY,2))
    if thief_dis < 50:return True
    return False

def parentscollision(playerX,playerY,parentX,parentY):
    parent_dis=math.sqrt(math.pow(parentX-playerX,2) + math.pow(parentY-playerY,2))
    if parent_dis < 50:return True
    return False

#gameloop
    
while True:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #player movements    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -0.2
            if event.key == pygame.K_RIGHT:
                playerXchange = +0.2
            if event.key == pygame.K_UP:
                playerYchange = -0.2
            if event.key == pygame.K_DOWN:
                playerYchange = +0.2

        if event.type == pygame.KEYUP:
            playerXchange = 0
            playerYchange = 0           

    #player boundary
    playerX += playerXchange
    playerY += playerYchange

    if playerX <= 0:
        playerX = 0
    elif playerX >= 536:
        playerX = 536
    if playerY <= 0:
        playerY =0
    elif playerY >= 636:
        playerY = 0

    #vehicle boundary
    
    #bike
    bikeX += bikeXchange
    
    if bikeX <= 0:
        bikeXchange = 0.6
    elif bikeX >= 600:
        bikeX = -50
        bikeXchange = -0.6
    
    #chopper
    chopperX += chopperXchange
    
    if chopperX <= 0:
        chopperXchange = 0.4
    elif chopperX >= 600:
        chopperX = -50
        chopperXchange = -0.4
    
    #police
    policeX += policeXchange
    
    if policeX <= 0:
        policeXchange = 0.5
    elif policeX >= 600:
        policeX = -50
        policeXchange = -0.5
    
    #banktruck
    btruckX += btruckXchange

    if btruckX <=0:
        btruckX=650
        btruckXchange = 0.7
    elif btruckX >= 700:
        btruckXchange = -0.7

    #thief
    thiefX += thiefXchange
    
    if thiefX <= 0:
        thiefXchange = 0.3
    elif thiefX >= 200:
        thiefXchange = -0.3
    
    #collision
    
    bike_collision = bikecollision(playerX,playerY,bikeX,bikeY)
    if bike_collision:
        playerX=300
        playerY=20
        messagebox.showinfo('cross it','you have been hit by a motorbike')

    chopper_collision = choppercollision(playerX,playerY,chopperX,chopperY)
    if chopper_collision:
        playerX=300
        playerY=20
        messagebox.showinfo('cross it','you have been hit by a copter')

    police_collision = policecollision(playerX,playerY,policeX,policeY)
    if police_collision:
        playerX=300
        playerY=20
        messagebox.showinfo('cross it','you have been hit by a police car')

    btruck_collision = banktruckcollision(playerX,playerY,btruckX,btruckY)
    if btruck_collision:
        playerX=300
        playerY=20
        messagebox.showinfo('cross it','you have been hit by a truck')
    
    pit_collision = pitcollision(playerX,playerY,pitX,pitY)
    if pit_collision:
        playerX=300
        playerY=20
        messagebox.showinfo('cross it','you fell in a pit')
    
    pit2_collision = pit2collision(playerX,playerY,pit2X,pit2Y)
    if pit2_collision:
        playerX=300
        playerY=20
        messagebox.showinfo('cross it','you fell in a pit')

    thief_collision = thiefcollision(playerX,playerY,thiefX,thiefY)
    if thief_collision:
        playerX=300
        playerY=20
        messagebox.showinfo('cross it','murdered by killer')

    parent_collision=parentscollision(playerX,playerY,parentX,parentY)
    if parent_collision:
        playerX=300
        playerY=20
        messagebox.showinfo('cross it','Hurrah! you reached your family safely..')
    
    parent()
    bike(bikeX,120)
    thief(thiefX,350)
    pit2(200,570)
    pit(350,350)
    chopper(chopperX,250)
    police(policeX,370)
    banktruck(btruckX,580)
    player(playerX,playerY)
    pygame.display.update()