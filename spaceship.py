from turtle import Turtle
from ammunition import Ammunition

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("White")
        self.shape("turtle")
        self.setheading(90)
        self.goto(0, -280)
        # x, y = self.position()
        # self.bullet = Ammunition(x, y)

    def move_forward(self):
        self.forward(15)

    def move_back(self):
        self.forward(-15)

    def right_shift(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def left_shift(self):
        new_x = self.xcor() - 40
        self.goto(new_x, self.ycor())

    def reset_player(self):
        self.goto(0, -280)

    def fire(self):
        x, y = self.position()
        bullet = Ammunition(x, y)
        # self.bullet.move_bullet()
