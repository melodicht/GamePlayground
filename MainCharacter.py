import arcade


class MainCharacter(arcade.AnimatedTimeSprite):
    gravity = 9.8
    velocity_y = 0

    def __init__(self, center_x, center_y):
        super.__init__(center_x=center_x, center_y=center_y)

    def update(self, dt=0):
        # If the character dies
        if self.is_dead:
            # TODO: Falls back animation, sfx, fx (smoke?)
            pass

        if not self.is_floored:
            self.velocity_y -= self.gravity
            self.center_y += self.velocity_y

    def check_is_floored(self):
        # If colliding with ground, true, else, false.
        # If false to true, sfx and fx, maybe sprite reaction?
        self.is_floored = True

    def check_death(self):
        # If collide with another object
        self.is_dead = True

    def jump(self):
        # If user hits spacebar
        # Jump animation, sfx and fx
        self.velocity_y = 60
