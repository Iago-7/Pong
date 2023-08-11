from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
LEFT_PADDLE_X_COORD = -350
RIGHT_PADDLE_X_COORD = 350
PADDLE_Y_COORD = 0
FRONT_OF_LEFT_PADDLE_X_COORD = -330
FRONT_OF_RIGHT_PADDLE_X_COORD = 330
SCREEN_UPPER_BOUND = 280
SCREEN_LOWER_BOUND = -280
LEFT_SIDE_BOUNDARY = -352
RIGHT_SIDE_BOUNDARY = 352
LEFT_SCOREBOARD_COORD = (-100, 260)
RIGHT_SCOREBOARD_COORD = (100, 260)
GAME_ENDING_SCORE = 5
SECONDS_DELAY_AFTER_POINT = 0.5
DISTANCE_FROM_PADDLE_FOR_PADDLE_BOUNCE = 50


screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")

left_paddle = Paddle(LEFT_PADDLE_X_COORD, PADDLE_Y_COORD)
right_paddle = Paddle(RIGHT_PADDLE_X_COORD, PADDLE_Y_COORD)

ball = Ball()

left_score = Scoreboard(LEFT_SCOREBOARD_COORD)
right_score = Scoreboard(RIGHT_SCOREBOARD_COORD)

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() >= SCREEN_UPPER_BOUND or ball.ycor() <= SCREEN_LOWER_BOUND:
        ball.y_direction_reversal()
    if ball.xcor() >= FRONT_OF_RIGHT_PADDLE_X_COORD:
        if right_paddle.distance(ball) <= DISTANCE_FROM_PADDLE_FOR_PADDLE_BOUNCE and ball.direction == "right":
            ball.direction = "left"
            ball.x_direction_reversal()
            ball.increase_speed()
        elif ball.xcor() >= RIGHT_SIDE_BOUNDARY:
            ball.reset_position()
            left_score.add_point()
            time.sleep(SECONDS_DELAY_AFTER_POINT)
    if ball.xcor() <= FRONT_OF_LEFT_PADDLE_X_COORD:
        if left_paddle.distance(ball) <= DISTANCE_FROM_PADDLE_FOR_PADDLE_BOUNCE and ball.direction == "left":
            ball.direction = "right"
            ball.x_direction_reversal()
            ball.increase_speed()
        elif ball.xcor() <= LEFT_SIDE_BOUNDARY:
            ball.reset_position()
            right_score.add_point()
            time.sleep(SECONDS_DELAY_AFTER_POINT)
    if left_score.score == GAME_ENDING_SCORE:
        game_is_running = False
        left_score.game_over("left")
    elif right_score.score == GAME_ENDING_SCORE:
        game_is_running = False
        right_score.game_over("right")


screen.exitonclick()
