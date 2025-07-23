from turtle import Turtle

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(0, -280)

    def move(self):
        self.forward(15)

    def reset_player(self):
        self.goto(0, -280)
