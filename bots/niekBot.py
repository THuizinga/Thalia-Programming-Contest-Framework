#!/usr/bin/python3

from random import Random

from bots.Bot import *

random = Random()


class Direction:
    East = 0
    West = 1
    North = 2
    South = 3

    offsets = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]


class ExampleBot(Bot):
    def __init__(self):
        super().__init__()
        self.placementIndex = 0
        # placementIndex is used to choose an island and shot location. You may remove it if you do not use it.

    # random, not along borders and euclidean distance of at least 4
    def choose_island_location(self):
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        for ix in range(-3, 4):
            for iy in range(-3 + abs(ix), 4 - abs(ix)):
                if self.enemyBoard.get((ix, iy)) != Tile.water:
                    return self.choose_island_location()

        return x, y

    # Random
    def choose_ship_location(self):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        direction = random.randint(0, 3)
        size = self.choose_ship_size()
        if self.checkFree((x, y), direction) < size:
            return self.choose_ship_location()
        return (x, y), \
               (x + Direction.offsets[direction] * (size - 1),
                y + Direction.offsets[direction] * (size - 1))

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

    def checkFree(self, coord, direction):
        result = 0
        x = coord[0]
        y = coord[1]
        ox = Direction.offsets[direction][0]
        oy = Direction.offsets[direction][1]

        for i in range(10):
            if x + ox * i < 0 or x + ox * i > 9 or \
                    y + oy * i < 0 or x + oy * i > 9:
                return result
            if self.ownBoard.get((x + ox * i, y + oy * i)).free:
                result += 1
            else:
                return result


if __name__ == "__main__":
    ExampleBot().run()
