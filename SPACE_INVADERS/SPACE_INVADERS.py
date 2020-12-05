import pygame,sys
import random
import math


#initialize the pygame
pygame.init()


#displaying screen with size
screen=pygame.display.set_mode((1000,600))


#display title 
pygame.display.set_caption('SPACE INVADERS')
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#bg
bg=pygame.image.load('bg.png')

#player
player_image=pygame.image.load('spaceship.png')
playerX=480
playerY=480
playerXchange=0

#enemy
enemy_image=[]
enemyX=[]
enemyY=[]
enemyXchange=[]
enemyYchange=[]
num_enemies=6
for i in range(num_enemies):
    enemy_image.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(50,900))
    enemyY.append(random.randint(50,80))
    enemyXchange.append(0.4)
    enemyYchange.append(30)

#bullet
bullet_image=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletYchange=4
bullet_state='ready'

#score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)

textX=8
textY=8

#gameover
over=pygame.font.Font('freesansbold.ttf',64)

def game_over():
    over_text=font.render('GAME OVER',True,(255,255,255))
    screen.blit(over_text,(400,300))
    
def show_score(x,y):
    score=font.render('Score:'+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(player_image,(x,y))

def enemy(x,y,i):
    screen.blit(enemy_image[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bullet_image,(x+20,y+10))

def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+ math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False
        
#game loop
while True:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                playerXchange = -2
            if event.key == pygame.K_RIGHT:
                playerXchange = +2
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                
        
        if event.type == pygame.KEYUP:
            playerXchange=0

    #player boundary
    playerX += playerXchange

    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936
        
    #enemy boundary
    for i in range(num_enemies):
        if enemyY[i] > 400:
            for j in range(num_enemies):
                enemyY[j]=2000
            game_over()
            break
        enemyX[i] += enemyXchange[i]
        if enemyX[i] <= 0:
            enemyXchange[i]=1
            enemyY[i] += enemyYchange[i]
        elif enemyX[i] >= 936:
            enemyXchange[i]= -1
            enemyY[i] +=enemyYchange[i]
        



        #collision
        collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY=480
            bullet_state='ready'
            score_value += 10
            enemyX[i]=random.randint(50,900)
            enemyY[i]=random.randint(50,80)


        enemy(enemyX[i],enemyY[i],i)

    #bullet bondary
    if bulletY <=0:
        bulletY = 480
        bullet_state ='ready'
    if bullet_state == 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletYchange

        
        
    
    player(playerX,playerY)
    show_score(textX,textY)  
    pygame.display.update()
        
