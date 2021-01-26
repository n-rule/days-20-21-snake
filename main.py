from turtle import Screen, Turtle
from snake import Snake
import time


screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.title('New Snake 3000')
screen.bgcolor('white')

snake = Snake(-150)

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')



game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.01)

    snake.move()

