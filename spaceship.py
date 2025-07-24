from turtle import Turtle

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("spaceship.gif")
        self.setheading(90)
        self.goto(0, -280)

    def move_forward(self):
        self.forward(15)

    def move_back(self):
        self.forward(-15)

    def right_shift(self):
        self.goto(self.xcor() + 30, self.ycor())

    def left_shift(self):
        self.goto(self.xcor() - 30, self.ycor())

    def reset_player(self):
        self.goto(0, -280)