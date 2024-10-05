import Fish


class Moly(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.name = name
        self.age = age
        self.directionV = directionV
        self.directionH = directionH
        self.width = 8
        self.height = 3
        self.x = x
        self.y = y

    def get_animal(self):
        moly = [[' ' for i in range(self.width)] for j in range(self.height)]
        for i in range(3, self.width - 1):
            moly[0][i] = '*'
            moly[2][i] = '*'
        for i in range(self.width):
            moly[1][i] = '*'
        for i in range(1):
            moly[0][i] = '*'
            moly[2][i] = '*'
        if self.directionH == 0:  # need to flip
            for i in range(self.height):
                moly[i].reverse()
        return moly
