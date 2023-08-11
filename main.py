from turtle import Screen
from paddle import Paddle
from ball import Ball


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
LEFT_PADDLE_X_COORD = -350
RIGHT_PADDLE_X_COORD = 350
PADDLE_Y_COORD = 0
FRONT_OF_LEFT_PADDLE_X_COORD = -330
FRONT_OF_RIGHT_PADDLE_X_COORD = 330
SCREEN_UPPER_BOUND = 280
SCREEN_LOWER_BOUND = -280
RIGHT_SIDE_BOUNDARY = 352
LEFT_SIDE_BOUNDARY = -352


screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")

left_paddle = Paddle(LEFT_PADDLE_X_COORD, PADDLE_Y_COORD)
right_paddle = Paddle(RIGHT_PADDLE_X_COORD, PADDLE_Y_COORD)

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
        ball.y_direction_reversal()
    if ball.xcor() >= FRONT_OF_RIGHT_PADDLE_X_COORD:
        if right_paddle.distance(ball) <= 50 and ball.direction == "right":
            ball.direction = "left"
            ball.x_direction_reversal()
        elif ball.xcor() >= 352:
            ball.reset_position()
            print("point left")
    if ball.xcor() <= FRONT_OF_LEFT_PADDLE_X_COORD:
        if left_paddle.distance(ball) <= 50 and ball.direction == "left":
            ball.direction = "right"
            ball.x_direction_reversal()
        elif ball.xcor() <= -352:
            ball.reset_position()
            print("point right")

screen.exitonclick()
