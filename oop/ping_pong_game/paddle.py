from turtle import Turtle


MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=350, y=0)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=350, y=new_y)
        
    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(x=350, y=new_y)

