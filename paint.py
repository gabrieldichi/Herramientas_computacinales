"""Paint, for drawing shapes and change width, color, shape.

Maximiliano Carrasco
Gabriel Dichi
Sebastian Joya

30/10/2020

"""

from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x -  start.x)#cuadr
        left(90) 
    end_fill()


def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    speed(0)
    for count in range(360):
        forward((end.x-start.x)/100)#circ
        left(1)
    end_fill()
    

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward((end.x) - (start.x)*2)
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    "It will draw a equilateral triangule"
    up()
    goto(start.x,start.y)
    down()
    begin_fill()

    for count in range (2):
        forward(end.x-start.x)
        forward(end.y-start.y)
        left(120)
    end_fill()
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value



state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
"width size selection"
onkey(lambda: pensize(1),'S')
onkey(lambda: pensize(5),'M')
onkey(lambda: pensize(10),'L')
onkey(undo, 'u')

"fig color"
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color ('yellow'),'Y')
onkey(lambda: color('red'), 'R')
"fig shape"
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
