# import colorgram
#
# colors = colorgram.extract('hirst_image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     rgb_colors.append(color_tuple)
# print(rgb_colors)

from turtle import Turtle, Screen
import random

color_list = [(202, 164, 109), (240, 245, 242), (236, 239, 243), (153, 75, 49), (222, 201, 136), (53, 94, 124),
              (171, 153, 41), (136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72),
              (145, 178, 148), (91, 73, 75), (233, 176, 165), (160, 143, 159), (54, 47, 50), (184, 205, 172),
              (35, 61, 75), (22, 85, 89), (146, 19, 21), (86, 146, 130), (38, 67, 91), (13, 72, 66), (106, 128, 155),
              (175, 99, 101), (176, 192, 209)]

tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
screen = Screen()
screen.colormode(255)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)


def draw_dots(columns):
    for i in range(columns):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


def create_painting(number_of_rows, number_of_cols):
    for _ in range(number_of_rows):
        draw_dots(number_of_cols)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(50 * number_of_cols)
        tim.setheading(360)


create_painting(12, 12)
screen.exitonclick()
