#!/usr/bin/python3

from exampleBot.Bot import *


class ExampleBot(Bot):
    def __init__(self):
        super().__init__()
        self.placementIndex = 0
        # placementIndex is used to choose an island and shot location. You may remove it if you do not use it.

    # Not along border, euclidean distance of at least 3
    def choose_island_location(self):
        pass

    def choose_ship_location(self):
        pass

    def choose_shot_location(self):
        pass

    def choose_ship_size(self):
        pass

    def handle_result(self, text):
        pass

    def handle_update(self, text):
        pass


if __name__ == "__main__":
    ExampleBot().run()
