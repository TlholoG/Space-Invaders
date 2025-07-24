from turtle import Screen
from spaceship import Spaceship
from scoreboard import ScoreBoard
from aliens import Alien
from ammomanager import AmmoManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.addshape("spaceship.gif")
alien_gifs = ["alien1.gif", "alien2.gif", "alien3.gif", "alien4.gif", "alien5.gif", "alien6.gif"]
for gif in alien_gifs:
    screen.addshape(gif)

spaceship = Spaceship()
scoreboard = ScoreBoard()
alien_list = [Alien() for _ in range(30)]
ammo = AmmoManager()


def fire_bullet():
    x, y = spaceship.position()
    ammo.fire(x, y)


screen.listen()
screen.onkey(spaceship.move_forward, "Up")
screen.onkey(spaceship.move_back, "Down")
screen.onkey(spaceship.left_shift, "Left")
screen.onkey(spaceship.right_shift, "Right")
screen.onkey(fire_bullet, "space")

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.level_speed)
    screen.update()

    for alien in alien_list:
        alien.move()
        if alien.distance(spaceship) < 30:
            scoreboard.game_over()
            game_is_on = False

    if spaceship.ycor() > 280:
        scoreboard.update_score()
        spaceship.reset_player()

    ammo.update_bullets()
    ammo.check_hits(alien_list)

screen.exitonclick()
