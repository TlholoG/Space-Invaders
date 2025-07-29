from ammunition import Ammunition


class AmmoManager:
    def __init__(self, scoreboard):
        self.bullets = []
        self.scoreboard = scoreboard

    def fire(self, x, y):
        bullet = Ammunition(x, y)
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets[:]:
            if bullet.isvisible():
                bullet.move_bullet()
            else:
                self.bullets.remove(bullet)

    def check_hits(self, aliens):
        # points = 0
        for bullet in self.bullets[:]:
            for alien in aliens[:]:
                if bullet.distance(alien) < 40:
                    bullet.hideturtle()
                    alien.hideturtle()
                    self.bullets.remove(bullet)
                    if alien.shape() == "alien1.gif":
                        points = 10
                    elif alien.shape() == "alien2.gif":
                        points = 20
                    elif alien.shape() == "alien3.gif":
                        points = 30
                    elif alien.shape() == "alien4.gif":
                        points = 40
                    elif alien.shape() == "alien5.gif":
                        points = 50
                    elif alien.shape() == "alien6.gif":
                        points = 60
                    elif alien.shape() == "alien7.gif":
                        points = 70
                    else:
                        points = 0

                    aliens.remove(alien)
                    self.scoreboard.update_score(points=points)
                    break  # Exit inner loop to avoid modifying list during iteration
