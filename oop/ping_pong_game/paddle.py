from turtle import Turtle
from typing import Tuple

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, coordinate: Tuple[float, float]):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinate)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y=new_y)
        
    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y=new_y)

