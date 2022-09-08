# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.turtlesize(5)
# timmy.color("red", "blue")
# timmy.fd(100)
# timmy.rt(100)
# timmy.lt(100)
# timmy.write("Hello World")
# print(my_screen.canvheight)
# my_screen.exitonclick()


# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def toString(self):
        return f"User(id = {self.id}, username = {self.username}, " \
               f"followers = {self.followers}, following = {self.following})"


user_1 = User("007", "bond")
user_2 = User("006", "james")
user_1.follow(user_2)
print(user_1.toString())
print(user_2.toString())
