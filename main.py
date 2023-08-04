from turtle import Screen
from paddle import Paddle


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


screen = Screen()
screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")

left_paddle = Paddle()

screen.listen()
screen.onkey(left_paddle.move_up(), "up")
screen.onkey(left_paddle.move_down(), "down")


screen.exitonclick()
