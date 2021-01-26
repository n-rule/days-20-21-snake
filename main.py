from turtle import Screen, Turtle
import time

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.title('New Snake 3000')
screen.bgcolor('white')

width = -20
segments = []

for _ in range(3):
    square = Turtle('square')
    square.penup()
    square.goto(width, 0)
    width += 20
    segments.append(square)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)