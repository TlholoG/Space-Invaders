from turtle import Screen
from spaceship import Spaceship
from ammunition import Ammunition
from aliens import Aliens
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

spaceship = Spaceship((100, -280))
initial_alien = -320
alien_level = 60
colors = ['red', 'blue', 'green', 'orange']
aliens = []
for color in colors:
    for _n in range(2):
        for _ in range(7):
            alien = Aliens((initial_alien, alien_level), color)
            aliens.append(alien)
            initial_alien += 105
        alien_level += 24
        initial_alien = -320


ammunition = Ammunition()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(spaceship.left_shift, "Left")
screen.onkey(spaceship.right_shift, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ammunition.move_speed)
    screen.update()
    ammunition.move()

    # Detect collision with wall
    if ammunition.xcor() > 380 or ammunition.xcor() < -380:
        ammunition.bounce_x()

    # Detect collision with spaceship
    if ammunition.distance(spaceship) < 50 and ammunition.ycor() < -250:
        ammunition.bounce_y()

    # Detectect collision with alien
    for enemy in aliens[:]:
        if ammunition.distance(enemy) < 40:
            ammunition.bounce_y()
            enemy.hideturtle()
            aliens.remove(enemy)
            scoreboard.add_point(enemy.color())
            scoreboard.update_scoreboard()
            break

    # Detect collision with top wall
    if ammunition.ycor() > 300:
        ammunition.bounce_y()

    # Detect spaceship miss
    if ammunition.ycor() < -280:
        ammunition.reset_position()
        game_is_on = False
        scoreboard.clear()
        scoreboard.final_score()


screen.exitonclick()