import arcade


class Obstacle(arcade.Sprite):
    speed = 5

    def __init__(self, image, center_x, center_y, scale=1):
        super().__init__(image, center_x=center_x,
                         center_y=center_y, scale=scale)

    def update(self):
        # If it goes off screen, remove it
        if self.right < 0:
            self.kill()

        self.center_x -= self.speed
