from turtle import Turtle


def Snake():
    width = -20
    segments = []

    for _ in range(3):
        square = Turtle('square')
        square.penup()
        square.goto(width, 0)
        width += 20
        segments.append(square)
