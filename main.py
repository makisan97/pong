from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=800)
screen.title('Pong')
screen.bgpic('background.gif')
screen.tracer(0)

left_paddle = Paddle((-370, 0))
right_paddle = Paddle((370, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.start_moving()
    
    # Detect collision with top wall
    if ball.ycor() > 385 or ball.ycor() <- 385:
        ball.bounce_wall()
    
    # Detect collision with paddle
    if (ball.distance(right_paddle) < 100 and ball.xcor() > 350) or (ball.distance(left_paddle) < 100 and ball.xcor() < -350):
        ball.bounce_paddle()

    # Goal
    if ball.xcor() > 370:
        ball.reset_ball()
        scoreboard.left_paddle_goal()
    
    # Goal
    if ball.xcor() < -370:
        ball.reset_ball()
        scoreboard.right_paddle_goal()
        
    # Check if game over (first to 3)
    if scoreboard.right_score == 3:
        game_is_on = False
        scoreboard.right_wins()
    elif scoreboard.left_score == 3:
        game_is_on = False
        scoreboard.left_wins()
        







screen.exitonclick()