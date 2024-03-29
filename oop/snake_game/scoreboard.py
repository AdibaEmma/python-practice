from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


def read_high_score():
    with open("data.txt") as file:
        return int(file.read())


def write_high_score(new_high_score):
    with open("data.txt", mode="w") as file:
        file.write(f"{new_high_score}")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_high_score()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            write_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()
