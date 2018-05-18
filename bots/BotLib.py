from _random import Random

from bots.Bot import Bot

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


class BotLib(Bot):
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
