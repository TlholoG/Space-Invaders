from turtle import Screen
from spaceship import Spaceship
from scoreboard import ScoreBoard
from aliens import Alien
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')

spaceship = Spaceship()
scoreboard = ScoreBoard()
alien_list = []
for _ in range(30):
    alien_list.append(Alien())

screen.listen()
screen.onkey(spaceship.move_forward, "Up")
screen.onkey(spaceship.move_back, "Down")
screen.onkey(spaceship.left_shift, "Left")
screen.onkey(spaceship.right_shift, "Right")
screen.onkey(spaceship.fire, "space")

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.level_speed)
    screen.update()

    for alien in alien_list:
        alien.move()
        if alien.distance(spaceship) < 30:
            scoreboard.game_over()
            game_is_on = False

    if spaceship .ycor() > 280:
        scoreboard.update_score()
        spaceship.reset_player()


screen.exitonclick()