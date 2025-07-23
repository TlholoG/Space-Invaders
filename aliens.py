from turtle import Turtle
class Aliens(Turtle):
    def __init__(self, position, colour):

        super().__init__()
        self.shape("square")
        self.color(colour)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.setheading(90)
