from turtle import Turtle


class Ammunition(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 17
        self.y_move = 17
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)  # Swap x and y around in the variable

    def bounce_y(self):
        self.y_move *= -1
        # self.move_speed *= 1.2

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(-50, -270)
        self.y_move = self.y_move * (-1)
        self.move()
        self.move_speed = 0.1
