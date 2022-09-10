# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#     def toString(self):
#         return f"User(id = {self.id}, username = {self.username}, " \
#                f"followers = {self.followers}, following = {self.following})"
#
#
# user_1 = User("007", "bond")
# user_2 = User("006", "james")
# user_1.follow(user_2)
# print(user_1.toString())
# print(user_2.toString())


from turtle import Turtle, Screen
from random import randint
from typing import Tuple

timmy = Turtle()


# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         timmy.forward(100)
#         timmy.right(angle)


def random_color() -> Tuple[int, int, int]:
    r = randint(0, 1)
    g = randint(0, 1)
    b = randint(0, 1)
    color = (r, g, b)
    return color


# for i in range(3, 11):
#     random_color = random_color()
#     timmy.color(random_color)
#     draw_shape(i)

timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(1)
my_screen = Screen()
my_screen.exitonclick()
