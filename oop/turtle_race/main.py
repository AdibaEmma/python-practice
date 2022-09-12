from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

distance = 10
angle = 10


def move_forwards():
    tim.forward(distance)


def move_backwards():
    tim.backward(distance)


def turn_right():
    tim.right(angle)


def turn_left():
    tim.left(angle)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.setpos(0, 0)
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
