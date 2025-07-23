from turtle import Turtle


class Spaceship(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.setheading(90)

    def right_shift(self):
        new_x = self.xcor() + 40
        self.goto(new_x, self.ycor())

    def left_shift(self):
        new_x = self.xcor() -40
        self.goto(new_x, self.ycor())

