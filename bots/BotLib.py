from bots.Bot import Bot


class Direction:
    East = 0
    South = 1
    West = 2
    North = 3

    offsets = [
        (1, 0),
        (0, -1),
        (-1, 0),
        (0, 1)
    ]


class BotLib(Bot):
    def checkRangeFree(self, coord, direction):
        x = coord[0]
        y = coord[1]
        ox = Direction.offsets[direction][0]
        oy = Direction.offsets[direction][1]

        for i in range(11):
            if not self.checkFree((x + ox * i, y + oy * i), self.ownBoard):
                return i

    def checkFree(self, coord, board, canBeOut=False):
        x = coord[0]
        y = coord[1]
        if x < 0 or x > 9 or y < 0 or y > 9:
            return canBeOut
        return board.get((x, y)).free
