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

timmy = Turtle()


# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

def draw_shape(num_sides):
    for i in range(num_sides):
        angle = 360 / num_sides
        timmy.forward(100)
        timmy.right(angle)


for i in range(3, 11):
    r = randint(0, 1)
    g = randint(0, 1)
    b = randint(0, 1)
    timmy.pencolor(r, g, b)
    draw_shape(i)

my_screen = Screen()
my_screen.exitonclick()
