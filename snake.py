"""Snake, classic arcade game with different modifications

Sebastin Joya
Maximiliano Carrasco
Gabriel Dichi

30/10/2020

"""
import random
from turtle import *
from random import randrange
from freegames import square, vector
speed=int(input('Please Write a number from 0 to 100 to chosee speed (while closer to the number 0, the speed would increase: '))
food = vector(0,0)
snake = [vector(10, 0)]
colors  = ["green","blue","orange","purple","pink","yellow"]
color = random.choice(colors)
color2 = random.choice(colors)
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head= snake[-1].copy()
    head.move(aim)
    i=0

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color)

    square(food.x, food.y, 9,color2)
    
    
    update()

    ontimer(move, speed)


setup(420, 420, 370,0)
hideturtle()
tracer(False)
listen()

"Snake move with alternative keys"
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')

move()
done()
