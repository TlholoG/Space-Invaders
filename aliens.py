from turtle import Turtle
import random
car_color = ["blue", "red", "purple", "yellow", "orange", "green", "brown", "pink"]

class Alien(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(car_color))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.goto(random.randint(-250, 250), random.randint(-250, 250))

    def move(self):
        if self.xcor() < -300:
            self.goto(300, random.randint(-250, 250))
        self.forward(2)
