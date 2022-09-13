from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

position_y = -70
for turtle_color in colors:
    tim = Turtle(shape="turtle")
    tim.color(turtle_color)
    tim.penup()
    tim.goto(x=-230, y=position_y)
    position_y += 30

# distance = 10
# angle = 10
# 
# 
# def move_forwards():
#     tim.forward(distance)
# 
# 
# def move_backwards():
#     tim.backward(distance)
# 
# 
# def turn_right():
#     tim.right(angle)
# 
# 
# def turn_left():
#     tim.left(angle)
# 
# 
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.setpos(0, 0)
#     tim.pendown()
# 
# 
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()
