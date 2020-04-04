import arcade

from Obstacle import Obstacle
import threading


class ObstacleManager:
    game_over = False

    def __init__(self, screen_width):
        self.screen_width = screen_width
        self.obstacle_list = arcade.SpriteList()
        event = threading.Event()
        self.periodic_spawn(event, 5)

    def periodic_spawn(self, event, delay_in_seconds):
        """Create obstacle instance every `delay_in_seconds`."""
        self.spawn_obstacle()
        if not event.is_set():
            threading.Timer(
                delay_in_seconds,
                self.periodic_spawn,
                [event, delay_in_seconds]
            ).start()

    def spawn_obstacle(self):
        obstacle_sprite = Obstacle(
            "resources/images/floor_block.png",
            scale=0.3,
            center_x=self.screen_width + 100,
            center_y=217
        )
        self.obstacle_list.append(obstacle_sprite)
