from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")

left_paddle = Paddle("Left")
right_paddle = Paddle("Right")

ball = Ball()


screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_is_running = True
ball.initial_move()
while game_is_running:
    screen.update()
    time.sleep(0.1)
    ball.move()



screen.exitonclick()
