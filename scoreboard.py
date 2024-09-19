from turtle import Turtle
FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=368)
        self.right_score = 0
        self.left_score = 0
        self.write(f'{self.left_score}  :  {self.right_score}', align=ALIGNMENT, font=FONT)
        
    def right_paddle_goal(self):
        self.right_score += 1
        self.clear()
        self.write(f'{self.left_score}  :  {self.right_score}', align=ALIGNMENT, font=FONT)
        
    def left_paddle_goal(self):
        self.left_score += 1
        self.clear()
        self.write(f'{self.left_score}  :  {self.right_score}', align=ALIGNMENT, font=FONT)
        
    def right_wins(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(f'  {self.left_score}  :  {self.right_score}\nRIGHT WINS!', align=ALIGNMENT, font=FONT)
        
    def left_wins(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(f'  {self.left_score}  :  {self.right_score}\nLEFT WINS!', align=ALIGNMENT, font=FONT)