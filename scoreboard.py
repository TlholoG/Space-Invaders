from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-60, 240)
        self.write(f"Top Score 980| Score: {self.score}", align="center", font=("Courier", 30, "normal"))

    def add_point(self, point_color):
        if point_color == ('red', 'red'):
            self.score += 10
        if point_color == ('blue', 'blue'):
            self.score += 15
        if point_color == ('green', 'green'):
            self.score += 20
        if point_color == ('orange', 'orange'):
            self.score += 25
        # self.score += 1
        self.clear()
        self.update_scoreboard()

    def final_score(self):
        self.goto(-100, 240)
        self.write(f"Final Score:{self.score}", align="center", font=("Courier", 40, "normal"))
