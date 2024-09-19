from turtle import Turtle
PADDLE_SPEED = 60

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=10)
        self.goto(position)
        self.score = 0
        
    def up(self):
        current_y = self.ycor()
        if current_y < 300:
            self.goto(x=self.xcor(), y=current_y+PADDLE_SPEED)
        
    def down(self):
        current_y = self.ycor()
        if current_y > -300:
            self.goto(x=self.xcor(), y=current_y-PADDLE_SPEED)