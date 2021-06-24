
import turtle
import math
from time import time
from random import randint

score = 0
pen = turtle.Turtle()
wn = turtle.Screen()
wn.setup(width=1645, height=1000, startx=None, starty=None)
wn.listen()
turtle.register_shape("images/spaceship2.gif")
turtle.register_shape("images/meteor.gif")
turtle.register_shape("images/meteor2.gif")
turtle.register_shape("images/meteor3.gif")
turtle.register_shape("images/score.gif")
turtle.register_shape("images/logo.gif")
pen.penup()
pen.setposition(-400, 400)
pen.pendown()  

for side in range(3):  
    pen.forward(800)
    pen.right(90)

pen.forward(800)
pen.hideturtle()

logo = turtle.Turtle()
logo.shape('images/logo.gif')
logo.penup()
logo.setposition(0, 450)

player = turtle.Turtle()
player.shape('images/spaceship2.gif')
player.penup()
player.setposition(0, -350)

score_board = turtle.Turtle()
score_board.shape('images/score.gif')
score_board.penup()
score_board.setposition(-340, 370)

enemies = []
for i in range(14):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    x = randint(-400, 400)
    y = randint(150, 320)
    meteor_shape = randint(1, 3)
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(x, y)

    if meteor_shape == 1:
        enemy.shape('images/meteor.gif')
    elif meteor_shape == 2:
        enemy.shape('images/meteor2.gif')
    elif meteor_shape == 3:
        enemy.shape('images/meteor3.gif')

bullet = turtle.Turtle()
bullet.color('yellow')
bullet.penup()
bullet.speed(0)
bullet.setheading(90) 
bullet.shapesize(2, 2)
bullet.hideturtle()
bullet_speed = 30
bullet_state = 'ready' 

turtle.color("black")
turtle.penup()
turtle.setposition(-350, 354)
turtle.write(": {}".format(score), move=False, align="left", font=("Arial", 24, "normal"))
turtle.hideturtle()


def right():
    x = player.xcor()
    x += 15
    if x > 350:
        x = 350
    player.setx(x)


def left():
    x = player.xcor()
    x -= 15
    if x < -350:
        x = -350
    player.setx(x)


def up():
    y = player.ycor()
    y += 15
    if y > 350:
        y = 350
    player.sety(y)


def down():
    y = player.ycor()
    y -= 15
    if y < -350:
        y = -350
    player.sety(y)


def fire_bullet():
   
    global bullet_state
    if bullet_state == 'ready':
        bullet_state = 'fire'
        x = player.xcor() 
        y = player.ycor() + 0.5  
        bullet.setposition(x, y)  
        bullet.showturtle()  


def isCollosion(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 35:
        return True
    else:
        return False


def enemyHit(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 35:
        return True
    else:
        return False


wn.onkey(right, 'Right')
wn.onkey(left, 'Left')
wn.onkey(up, 'Up')
wn.onkey(down, 'Down')
wn.onkey(fire_bullet, 'space')

wn.bgpic("images/space.gif")

enemy_speed = 4  
while True:
    for enemy in enemies:  

        if isCollosion(player, enemy):
            player.hideturtle() 
            turtle.color('red')
            turtle.penup()
            turtle.setposition(0, 0)
            turtle.write("Game Over!", move=False, align="center", font=("Arial", 35, "normal"))
            turtle.setposition(0, -50)
            turtle.write("Your score is: {}".format(score), move=False, align="center", font=("Arial", 35, "normal"))
            turtle.done()
            break

        if enemyHit(bullet, enemy):
            bullet.hideturtle()
            bullet_state = 'ready'
            y = randint(-150, 320)
            enemy.setposition(-400, y)
            score += 1
            turtle.clear()

            turtle.color("black")
            turtle.penup()
            turtle.setposition(-350, 354)
            turtle.write(": {}".format(score), move=False, align="left", font=("Arial", 24, "normal"))
            turtle.hideturtle()

        if enemy.xcor() > 370:  
            y = enemy.ycor() 
            y -= 40  
            enemy.sety(y) 
            enemy.speed(0)  
            enemy.setx(-370) 

        if enemy.ycor() < -360: 
            y = 400  
            enemy.speed(0)  
            enemy.sety(y)  

        if bullet_state == 'fire':
            y = bullet.ycor()  
            y += bullet_speed  
            bullet.sety(y)  

        if bullet.ycor() > 275: 
            bullet.hideturtle() 
            bullet_state = 'ready'  

        x = enemy.xcor()  
        x += enemy_speed
        enemy.setx(x)  

turtle.done()
turtle.close()