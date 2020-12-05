import turtle
import time
import random

delay=0.05

#creating screen
win=turtle.Screen()
win.title('SNAKE_GAME')
win.bgcolor('black')
win.setup(600,600)
win.tracer(0)

body=[]
score=0
#snake
head=turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('white')
head.penup()
head.goto(0,0)
head.direction='stop'
x=head.xcor()
y=head.ycor()
#food
food=turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('red')
food.penup()
food.goto(0,100)

#score
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('yellow')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Score:0',align='center',font=('courier',20,'normal'))

#movement function
def go_up():
    head.direction='up'
def go_down():
    head.direction='down'
def go_right():
    head.direction='right'
def go_left():
    head.direction='left'
    

#move
def move():
    if head.direction=='up':
        Y=head.ycor()
        head.sety(Y+20)
    if head.direction=='down':
        Y=head.ycor()
        head.sety(Y-20)
    if head.direction=='right':
        X=head.xcor()
        head.setx(X+20)
    if head.direction=='left':
        X=head.xcor()
        head.setx(X-20)

#keyboard inputs
win.listen()
win.onkeypress(go_up,"Up")
win.onkeypress(go_down,"Down")
win.onkeypress(go_right,"Right")
win.onkeypress(go_left,"Left")


#gameloop
while True:
    win.update()

    if x >290 or x<-290 or y>290 or y<-290:
        time.sleep(0.5)
        head.goto(0,0)

    if head.distance(food)<20:
        #move the food to random place
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #newbody
        newbody=turtle.Turtle()
        newbody.speed(0)
        newbody.shape('circle')
        newbody.color('gray')
        newbody.penup()
        body.append(newbody)
        # the score
        score+=10
        pen.clear()
        pen.write('Score:{}'.format(score),align='center',font=('courier',20,'normal'))
        
        #increasing length of the body
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)

    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)

    move()

    for i in body:
        if i.distance(head)<20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction='stop'

            for i in body:
                i.goto(1000,1000)

            body.clear()
            score=0
            pen.clear()
            pen.write('Score:{}'.format(score),align='center',font=('courier',20,'normal'))
        

            
    time.sleep(delay)


win.mainloop()







