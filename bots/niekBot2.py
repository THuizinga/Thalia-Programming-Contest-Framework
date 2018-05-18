#!/usr/bin/python3
from random import randint
from sys import stderr

from bots.BotLib import BotLib, Direction

matrix = [[0 for x in range(10)] for y in range(10)]
class NiekBot(BotLib):
    def __init__(self):
        super().__init__()
        # placementIndex is used to choose an island and shot location. You may remove it if you do not use it.

    # random, not along borders and euclidean distance of at least 4
    def choose_island_location(self):
        x = randint(1, 9)
        y = randint(1, 9)
        for ix in range(-3, 4):
            for iy in range(-3 + abs(ix), 4 - abs(ix)):
                if not self.checkFree((x + ix, y + iy), self.enemyBoard, True):
                    return self.choose_island_location()

        return x, y

    # Random
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
            elif dir == 0 and x1 < 8:
                    x1 += 2
            elif dir == 0 and x1 < 9:
                    x1 += 1
            elif dir == 1 and y1 < 8:
                    y1 += 2
            elif dir == 1 and y1 < 9:
                    y1 += 1
            elif dir == 2 and x1 > 1:
                    x1 -= 2
            elif dir == 2 and x1 > 0:
                    x1 -= 1
            elif dir == 3 and y1 > 1:
                    y1 -= 2
            elif dir == 3 and y1 > 0:
                    y1 -= 1
            elif (y1==1 or y1 ==2) and x1 == 0:
                x = randint(0, 9)
                y = randint(0, 9)
                direction = randint(0, 3)
                print(shipSize, file=stderr)
                if self.checkRangeFree((x, y), direction) < shipSize:
                    return self.choose_ship_location(shipSize)
                thing = ((x, y), \
                         (x + Direction.offsets[direction][0] * (shipSize - 1),
                          y + Direction.offsets[direction][1] * (shipSize - 1)))
                print(thing, file=stderr)
                return thing

            else:
                print('eee', file=stderr)
                dir = (dir + 1) % 4



    # Chance field
    def choose_shot_location(self):
        x = randint(0, 9)
        y = randint(0, 9)
        while matrix[x][y] == 1:
            x = randint(0, 9)
            y = randint(0, 9)


        # scores = [[sum([min(5, self.checkRangeFree((x, y), d)) for d in range(0, 4)])
        #           for y in range(0, 10)]
        #          for x in range(0, 10)]
        #
        # max=0
        # x=0
        # y=0
        # for x in range(0,10):
        #     for y in range(0,10):
        #         if max < scores[x][y]:
        #             max = scores[x][y]:
        #
        # print(scores, file=sys.stderr)
        matrix[x][y] = 1
        return x, y

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
