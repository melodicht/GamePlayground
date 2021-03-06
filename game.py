"""Starting Template

"""
import arcade

from MainCharacter import MainCharacter
from ObstaclesManager import ObstacleManager


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"


class MyGame(arcade.Window):
    """Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """Create sprites."""
        # Character sprite
        self.player_sprite = MainCharacter(190, 217)

        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Ground sprites
        self.ground_list = arcade.SpriteList()
        ground_width = 128
        ground_range = SCREEN_WIDTH // ground_width + 1
        for i in range(ground_range):
            self.ground_sprite = arcade.Sprite(
                "resources/images/floor_block.png",
                center_x=i*ground_width,
                center_y=25
            )
            self.ground_list.append(self.ground_sprite)

        self.obstacle_manager = ObstacleManager(SCREEN_WIDTH)

        self.player_sprite.ground_list = self.ground_list
        self.player_sprite.obstacle_list = self.obstacle_manager.obstacle_list

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()
        self.ground_list.draw()
        self.obstacle_manager.obstacle_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player_list.update_animation()
        self.player_sprite.update()
        self.obstacle_manager.obstacle_list.update()

    def on_key_press(self, key, key_modifiers):
        """Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """Called whenever the user lets off a previously pressed key."""
        # If the player hits 'SPACE' while on the floor
        jumpable = (key == 32 and self.player_sprite.is_floored)
        if jumpable:
            self.player_sprite.jump()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """Called whenever the mouse moves."""
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """Called when the user presses a mouse button."""
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """Called when a user releases a mouse button."""
        pass


def main():
    """Main method."""
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
