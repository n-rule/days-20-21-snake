from turtle import Turtle

snake_speed = 20

class Snake:
    def __init__(self, starting_y):
        """Starting y = starting point"""
        self.width = starting_y
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            square = Turtle('square')
            square.penup()
            square.goto(self.width, 0)
            self.width += 20
            self.segments.append(square)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(snake_speed)


    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)
