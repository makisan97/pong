from turtle import Turtle
import random
BALL_SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def start_moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)
        
    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        
    def reset_ball(self):
        self.goto(x=0, y=0)
        self.x_move *= -1
            
            