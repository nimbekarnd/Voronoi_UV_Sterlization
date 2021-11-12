# To calculate the robots required per room and the total robots for the mission.

import sys
for line in sys.path:
    print(line)


class Area:
    def __init__(self, bot, box):
        self.bot = bot
        self.box = box
        self.width = box[0]
        self.height = box[1]

    def calculate(self):
        w = self.width
        h = self.height
        area = w * h
        return area

    def compare(self):
        area_bot = 10 * self.bot[0] * self.bot[1]  # Bot can cover 10 square meter space in one round
        area_room = Area.calculate(self)

        n = area_room // area_bot
        if n == 0:
            n = 1
        else:
            pass
        return n

