# Austin HACK

from random import choice, random
from turtle import *

from freegames import vector


def value():
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 4) * choice([1, -1])


global a, b
a = value()
b = value()
ball = vector(0, 0)
aim = vector(a, b)
state = {1: 0, 2: 0}


def move(player, change):
    "Move player position by change."
    state[player] += change


def rectangle(x, y, width, height):
    "Draw rectangle at (x, y) with given width and height."
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
        color = [1, 0, 0.5]
    end_fill()


def draw():
    "Draw game and move pong ball."
    clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)
    rectangle(-10, -900, 10, 2000)

    ball.move(aim)
    x = ball.x
    y = ball.y

    up()
    goto(x, y)
    dot(10)
    update()

    if y < -200 or y > 200:
        aim.y = -aim.y
        update()

    if x < -185:
        low = state[1]
        high = state[1] + 50
        update()

        if low <= y <= high:
            aim.x = -aim.x
            update()
        else:
            return
            update()

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
            update()
        else:
            return
            update()

    ontimer(draw, 50)
    update()


def mainloop(a, b):
    while True:
        ball = vector(0, 0)
        aim = vector(a, b)
        state = {1: 0, 2: 0}
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        listen()
        onkey(lambda: move(1, 20), "w")
        onkey(lambda: move(1, -20), "s")
        onkey(lambda: move(2, 20), "i")
        onkey(lambda: move(2, -20), "k")
        a += 5
        b += 5
        draw()
        update()
        done()
        pass


mainloop(a, b)
