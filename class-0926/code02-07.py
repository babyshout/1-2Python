# code02-07.py

import turtle
import random


def screen_left_click(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)


def screen_right_click(x, y):
    turtle.penup()
    turtle.goto(x, y)


def screen_mid_click(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()


pSize, tSize = 10, 0
r, g, b = 0.0, 0.0, 0.0

turtle.title("거북이 그림 그리기")
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screen_left_click, 1)
turtle.onscreenclick(screen_mid_click, 2)
turtle.onscreenclick(screen_right_click, 3)

turtle.done()
