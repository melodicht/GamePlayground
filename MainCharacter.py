import arcade


class MainCharacter(arcade.AnimatedTimeSprite):
    gravity = 0.3
    velocity_y = 0
    is_floored = True
    is_dead = False

    def __init__(self, center_x, center_y):
        super().__init__(center_x=center_x, center_y=center_y)

        # Create sprite animation
        for i in range(7):
            texture = arcade.load_texture(
                "resources/images/running_man.png",
                x=i*128,
                y=0,
                width=128,
                height=128
            )
            self.textures.append(texture)

    def update(self, dt=0, ground_level=100):
        # If the character dies
        if self.is_dead:
            # TODO: Falls back animation, sfx, fx (smoke?)
            pass

        self.check_is_floored(ground_level)

        if not self.is_floored:
            self.velocity_y -= self.gravity
            self.center_y += self.velocity_y

    def check_is_floored(self, ground_level):
        # If colliding with ground, true, else, false.
        # If false to true, sfx and fx, maybe sprite reaction?
        if self.center_y < ground_level:
            self.center_y = ground_level
            self.velocity_y = 0
            self.is_floored = True

    def check_death(self):
        # If collide with another object
        self.is_dead = True

    def jump(self):
        # Jump animation, sfx and fx
        self.velocity_y = 10
        self.is_floored = False
