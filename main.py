from turtle import Screen
from paddle import Paddle
from ball import Ball


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
LEFT_PADDLE_X_COORD = -350
RIGHT_PADDLE_X_COORD = 350
Y_COORD = 0


screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")

left_paddle = Paddle(LEFT_PADDLE_X_COORD, Y_COORD)
right_paddle = Paddle(RIGHT_PADDLE_X_COORD, Y_COORD)

ball = Ball()

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_is_running = True
while game_is_running:
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    if ball.xcor() >= 350:
        if right_paddle.distance(ball) <= 50:
            ball.paddle_bounce()
        elif ball.xcor() >= 352:
            print("point left")
            game_is_running = False
    if ball.xcor() <= -350:
        if left_paddle.distance(ball) <= 50:
            ball.paddle_bounce()
        elif ball.xcor() <= -352:
            print("point right")
            game_is_running = False

screen.exitonclick()
