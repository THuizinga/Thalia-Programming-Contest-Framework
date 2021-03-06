#!/usr/bin/python3
from sys import stderr

from bots.Bot import *
from bots.BotLib import *


class ExampleBot(BotLib):
    def __init__(self):
        super().__init__()
        self.placementIndex = 0
        # placementIndex is used to choose an island and shot location. You may remove it if you do not use it.

    def choose_ship_location(self):
        # This method places the ships in a spiral starting from outside to the inside.

        shipSize = self.choose_ship_size() - 1
        # Choose the ship's left position
        x1=0
        x2=0
        y1=0
        y2=0
        dir = 0
        while shipSize > 0:
            if self.checkRangeFree((x1,y1),dir) > shipSize:
                x2 = x1 + Direction.offsets[dir][0]*shipSize
                y2 = y1 + Direction.offsets[dir][1]*shipSize
                print(x1, file=stderr)
                print(y1, file=stderr)
                print(x2, file=stderr)
                print(y2, file=stderr)
                return ((x1,y1),(x2,y2))
            elif dir == 0 and x1 < 9:
                    x1 += 1
                    print('a', file=stderr)
            elif dir == 1 and y1 < 9:
                    y1 += 1
                    print('b', file=stderr)
                    print(y1, file=stderr)
            elif dir == 2 and x1 > 0:
                    x1 -= 1
                    print('c', file=stderr)
            elif dir == 3 and y1 > 0:
                    print('d', file=stderr)
                    y1 -= 1
            else:
                print('eee', file=stderr)
                dir = (dir + 1) % 4




    def choose_island_location(self):
        # This is a dummy method, you should write a better one.
        self.placementIndex += 1
        return (int(self.placementIndex / 10), self.placementIndex % 10)

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
    ExampleBot().run()
