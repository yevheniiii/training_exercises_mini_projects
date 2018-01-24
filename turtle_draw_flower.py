# -*- coding: utf-8 -*-
import turtle


def initials(some_art):
    for i in range(1, 5):
        some_art.forward(100)
        some_art.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor('black')
    init = turtle.Turtle()
    init.shape('turtle')
    init.color('white')
    init.speed(5)
    for i in range(1, 37):
        initials(init)
        init.right(10)
    init.right(90)
    init.forward(250)

    window.exitonclick()


draw_art()
