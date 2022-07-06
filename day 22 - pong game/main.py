from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_score = Scoreboard((50, 250))
l_score = Scoreboard((-50, 250))

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)

    l_score.write_score()
    r_score.write_score()
    r_paddle.move_up()
    r_paddle.move_down()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    
    if ball.xcor() > 320 or ball.xcor() < -320:
        if ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50:
            ball.x_bounce()

    if ball.xcor() > 350:
        ball.restart()
        l_score.increase_score()
    elif ball.xcor() < -350:
        ball.restart()
        r_score.increase_score()

   
screen.exitonclick()