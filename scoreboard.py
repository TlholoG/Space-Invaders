from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 1
        self.level_speed = 0.1
        self.write(f"Level: {self.score}", align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="center", font=("Arial", 20, "normal"))
        self.level_speed *= 0.5

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))

