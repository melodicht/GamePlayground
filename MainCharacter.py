import arcade


class MainCharacter(arcade.AnimatedTimeSprite):
    gravity = 0.3
    velocity_y = 0
    is_floored = True
    is_dead = False
    ground_list = []
    obstacle_list = []

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

    def update(self, dt=0):
        # If the character dies
        if self.is_dead:
            # TODO: Falls back animation, sfx, fx (smoke?)
            pass

        # Deals with jumping physics
        self.check_is_floored()
        if not self.is_floored:
            self.velocity_y -= self.gravity
            self.center_y += self.velocity_y

        # Deals with player colliding with obstacles
        self.check_death()

    def check_is_floored(self):
        # If colliding with ground, true, else, false.
        # If false to true, sfx and fx, maybe sprite reaction?
        hit = arcade.check_for_collision_with_list(
            self, self.ground_list
        )

        if not self.is_floored and any(hit):
            self.velocity_y = 0
            self.is_floored = True

    def check_death(self):
        # If collide with another object
        hit = arcade.check_for_collision_with_list(
            self, self.obstacle_list
        )

        if any(hit):
            # Death animation, sfx, fx, stop game
            self.is_dead = True

    def jump(self):
        # Jump animation, sfx and fx
        self.center_y += 10  # So it won't collide with the ground
        self.velocity_y = 10
        self.is_floored = False
