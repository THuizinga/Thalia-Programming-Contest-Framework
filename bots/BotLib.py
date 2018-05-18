from bots.Bot import Bot


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
    def checkRangeFree(self, coord, direction):
        x = coord[0]
        y = coord[1]
        ox = Direction.offsets[direction][0]
        oy = Direction.offsets[direction][1]

        for i in range(11):
            if x + ox * i < 0 or x + ox * i > 9 or \
                    y + oy * i < 0 or x + oy * i > 9:
                return i
            if not self.checkFree((x + ox * i, y + oy * i), self.ownBoard):
                return i

    def checkFree(self, coord, board, canBeOut=False):
        x = coord[0]
        y = coord[1]
        if x < 0 or x > 9 or y < 0 or y > 9:
            return canBeOut
        return board.get((x, y)).free
