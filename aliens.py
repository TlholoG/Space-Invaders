from turtle import Turtle
import random
alien_color = ["blue", "red", "purple", "yellow", "orange", "green", "brown", "pink"]

class Alien(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(alien_color))
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(270)
        self.goto(random.randint(-250, 250), random.randint(150, 350))

    def move(self):
        self.forward(random.randint(0, 5))

