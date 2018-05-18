#!/usr/bin/python3
from random import randint
from sys import stderr

from bots.BotLib import BotLib, Direction


class NiekBot(BotLib):
    def __init__(self):
        super().__init__()
        self.placementIndex = 0
        # placementIndex is used to choose an island and shot location. You may remove it if you do not use it.

    # random, not along borders and euclidean distance of at least 4
    def choose_island_location(self):
        x = randint(1, 8)
        y = randint(1, 8)
        for ix in range(-3, 4):
            for iy in range(-3 + abs(ix), 4 - abs(ix)):
                if not self.checkFree((x + ix, y + iy), self.enemyBoard, True):
                    return self.choose_island_location()

        return x, y

    # Random
    def choose_ship_location(self, size=None):
        if size is None:
            size = self.choose_ship_size()
        x = randint(0, 9)
        y = randint(0, 9)
        direction = randint(0, 3)
        print(size, file=stderr)
        if self.checkRangeFree((x, y), direction) < size:
            return self.choose_ship_location(size)
        thing = ((x, y), \
                 (x + Direction.offsets[direction][0] * (size - 1),
                  y + Direction.offsets[direction][1] * (size - 1)))
        print(thing, file=stderr)
        return thing

    # Chance field
    def choose_shot_location(self):
        # This is a dummy method, you should write a better one.
        self.placementIndex += 1
        return (int(self.placementIndex / 10), self.placementIndex % 10)

    def choose_ship_size(self):
        return super().choose_ship_size()
        # You may want to extend this method, but it is not required.

    def handle_result(self, text):
        super().handle_result(text)
        # You may want to extend this method, but it is not required.

    def handle_update(self, text):
        super().handle_update(text)
        # You may want to extend this method, but it is not required.


if __name__ == "__main__":
    # try:
    NiekBot().run()
# except:
# time.sleep(100)
