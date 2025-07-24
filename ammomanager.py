from ammunition import Ammunition


class AmmoManager:
    def __init__(self):
        self.bullets = []

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
        for bullet in self.bullets[:]:
            for alien in aliens[:]:
                if bullet.distance(alien) < 20:
                    bullet.hideturtle()
                    alien.hideturtle()
                    self.bullets.remove(bullet)
                    aliens.remove(alien)
                    break  # Exit inner loop to avoid modifying list during iteration
