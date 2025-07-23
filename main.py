from turtle import Screen
from spaceship import Spaceship
from scoreboard import ScoreBoard
from aliens import Alien
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

spaceship = Spaceship()
scoreboard = ScoreBoard()
alien_list = []
for _ in range(15):
    alien_list.append(Alien())

screen.listen()
screen.onkey(spaceship .move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.level_speed)
    screen.update()

    for vehicle in alien_list:
        vehicle.move()
        if vehicle.distance(spaceship) < 30:
            scoreboard.game_over()
            game_is_on = False

    if spaceship .ycor() > 280:
        scoreboard.update_score()
        spaceship.reset_player()


screen.exitonclick()