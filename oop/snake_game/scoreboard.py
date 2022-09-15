from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 260)
        self.update_scoreboard(f"Score: {self.score}")

    def update_scoreboard(self, text):
        self.write(text, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard(f"Score: {self.score}")

    def game_over(self):
        self.goto(0, 0)
        self.update_scoreboard("Game Over")
