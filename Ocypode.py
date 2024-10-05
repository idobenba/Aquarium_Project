import Crab


class Ocypode(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.width = 7
        self.height = 4

        self.directionH = directionH


    def get_animal(self):
        ocypode = [[' ' for i in range(self.width)] for j in range(self.height)]
        ocypode[0][1] = '*'
        ocypode[0][self.width-2] = '*'
        for i in range(2,5):  # line 1
            ocypode[1][i] = '*'
        for i in range(7):  # line 2
            ocypode[2][i] = '*'
        ocypode[3][0] = '*'
        ocypode[3][self.width-1] = '*'
        return ocypode

