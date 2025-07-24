from turtle import Turtle


class Ammunition(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(x, y)
        self.y_move = 17
        self.move_bullet()

    def move_bullet(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)
        # Keep moving every 50 milliseconds
        if self.ycor() < 300:  # Stop bullet when it leaves the screen
            self.getscreen().ontimer(self.move_bullet, 50)
        else:
            self.hideturtle()
            self.clear()


    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)  # Swap x and y around in the variable
        # self.forward(40)

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
