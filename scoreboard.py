from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-200, 240)
        self.color("black")
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Level = {self.level}", False, align="center", font=FONT)

    def score_increase(self):
        self.level += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER!", False, align="center", font=FONT)