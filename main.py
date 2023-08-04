from turtle import Screen
from paddle import Paddle


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")

left_paddle = Paddle("Left")
right_paddle = Paddle("Right")

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_is_running = True
while game_is_running:
    screen.update()


screen.exitonclick()
