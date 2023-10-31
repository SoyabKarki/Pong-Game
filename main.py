from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("PONG")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.update()

screen.listen()

# Controls for right paddle
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

# Controls for left paddle
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    screen.update()

    ball_position = ball.ycor()
    # Detect collision with wall
    if ball_position >= 280 or ball_position <= -280:
        ball.wall_bounce()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    # Detect ball miss
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()

    ball.move_ball()

    # Check if game over
    if scoreboard.l_score == 10:
        game_over = True
        scoreboard.game_over()

screen.exitonclick()
