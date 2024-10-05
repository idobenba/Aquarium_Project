import Crab


class Shrimp(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.name = name
        self.age = age
        self.x = x

        self.width = 7
        self.height = 3

        self.directionH = directionH


    def get_animal(self):
        shrimp = [[' ' for i in range(self.width)] for j in range(self.height)]
        shrimp[0][6] = '*'
        shrimp[0][2] = '*'
        for i in range(6):
            shrimp[1][i] = '*'
        shrimp[2][2] = '*'
        shrimp[2][4] = '*'

        if self.directionH == 0 :   # need to flip
            for i in range(self.height):
                shrimp[i].reverse()


        return shrimp

# shrimp1 = Shrimp('ert',12,2,2,0)
# shrimp1.get_animal()