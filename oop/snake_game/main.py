from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

position_x = 0
for turtle_body in range(0, 3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.goto(x=position_x, y=0)
    position_x -= 20












screen.exitonclick()
