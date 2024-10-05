import Fish


class Scalar(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.width = 8
        self.height = 5
        self.directionH = directionH

    def get_animal(self):
        scalar = [[' ' for i in range(self.width)] for j in range(self.height)]
        for i in range(self.width - 2):
            scalar[0][i] = '*'
            scalar[self.height-1][i] = '*'
        for i in range(4,self.width-1):
            scalar[1][i] = '*'
            scalar[3][i] = '*'
        for i in range(2,self.width):
            scalar[2][i] = '*'

        if self.directionH == 0 :   # need to flip
            for i in range(self.height):
                scalar[i].reverse()
        return scalar