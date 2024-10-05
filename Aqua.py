import Animal
import Fish
import Crab
import Shrimp
import Scalar
import Moly
import Ocypode

MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
FEED_AMOUNT = 10
MAX_AGE = 120



class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = [' '] * self.aqua_height
        self.build_tank()
        self.anim = []   # array of objects from type 'Animal'

    def build_tank(self):
        arr_board = [[' ' for i in range(self.aqua_width)] for j in range(self.aqua_height)]
        for row in range(self.aqua_height-1):
            arr_board[row][0] = '|'
            arr_board[row][self.aqua_width-1] = '|'

        arr_board[self.aqua_height-1][0] = "\\"
        arr_board[self.aqua_height - 1][self.aqua_width-1] = '/'
        for i in range(1,self.aqua_width-1):
            arr_board[self.aqua_height - 1][i] = '_'
        for i in range(1,self.aqua_width-1):  ## Adding water line
            arr_board[WATERLINE-1][i] = '~'

        self.board = arr_board


    def print_board(self):
        rows = []
        for row in self.board:
            rows.append(' '.join(str(x) for x in row))
        print('\n'.join(rows))

    def get_board(self):
        return self.board

    def get_all_animal(self):
        """
        Returns the array that contains all the animals
        """
        return self.anim

    def is_collision(self, animal):
        """
        Returns True if the next step of the crab is a collision
        """
        if not isinstance(animal, Crab.Crab):
            print("not valid")
            return
        crab_direction = animal.get_directionH()
        crab_position = animal.get_position()[0]
        next_crab_position = crab_position
        if crab_direction == 0: ## move to the left
            next_crab_position -=  1
        else: ### move to the right
            next_crab_position += 1
        for anim2 in self.anim:
            if isinstance(anim2, Crab.Crab):
                anim2_direction = anim2.get_directionH()
                anim2_position = anim2.get_position()[0]
                next_anim2_position = anim2_position
                if anim2_direction == 0: ## move left
                    next_anim2_position -= 1
                else: ### move right
                    next_anim2_position += 1
                if crab_direction == anim2_direction:
                    continue  #continue to next anim - iteration
                else:
                    if next_crab_position < next_anim2_position and crab_direction == 1:
                        if next_crab_position + animal.width  == next_anim2_position:
                            return True
                    elif next_crab_position > next_anim2_position and crab_direction == 0:
                        if next_anim2_position + anim2.width  == next_crab_position:
                            return True
                    if next_crab_position < next_anim2_position and crab_direction == 1:
                        if next_crab_position + animal.width  == next_anim2_position:
                            return True
                    elif next_crab_position > next_anim2_position and crab_direction == 0:
                        if next_anim2_position + anim2.width  == next_crab_position:
                            return True



        return False



    def print_animal_on_board(self, animal: Animal):
        str_animal = animal.get_animal()
        for i in range(animal.height):  # we iterate on animal rows
            for j in range(animal.width):  # we iterate on animal columns
                self.board[animal.y + i][animal.x + j] = str_animal[i][j]  # copy string on the cell
        # j = len(str_animal[0])
        # for i in range(len(str_animal)):
        #     self.board[animal.y+i][animal.x:animal.x+j] = str_animal[i][:j]
        return



    def delete_animal_from_board(self, animal: Animal):
        for i in range(animal.height):  # we iterate on animal rows
            for j in range(animal.width):  # we iterate on animal columns
                self.board[animal.y + i][animal.x + j] = ' '  # copy string on the cell
        return



    def add_fish(self, name, age, x, y, directionH, directionV, fishtype):
        """
        Adding fish to the aquarium
        """
        new_fish = '' #### need?
        if fishtype == 'sc':
            new_fish = Scalar.Scalar(name, age, x, y, directionH, directionV)
            if self.aqua_height >= y and y+new_fish.height >= self.aqua_height-5: # reaches the crabs line
                y = self.aqua_height -4 -new_fish.height
                new_fish.set_y(y)
            if self.aqua_width > x and x+new_fish.width >= self.aqua_width:  # reaches the right quarium edge
                x = self.aqua_width -new_fish.width-1
                new_fish.set_x(x)
        elif fishtype == 'mo':
            new_fish = Moly.Moly(name, age, x, y, directionH, directionV)
            if self.aqua_height >= y and y+new_fish.height >= self.aqua_height-5:  # reaches the crabs line
                y = self.aqua_height -4 -new_fish.height
                new_fish.set_y(y)
            if self.aqua_width > x and x+new_fish.width >= self.aqua_width:  # reaches the right quarium edge
                x = self.aqua_width -new_fish.width-1
                new_fish.set_x(x)
        else:
            print('wrong fishtype input, please try again')
            return False
        if not self.check_if_free(x,y):
            return False
        self.anim.append(new_fish)  # add new fish into list animals
        self.print_animal_on_board(new_fish)  # add new fish on board
        return True



    def add_crab(self, name, age, x, y, directionH, crabtype):
        """
        Adding crab to the aquarium
        """
        new_crab = '' ### need?
        if crabtype == 'oc':
            new_crab = Ocypode.Ocypode(name, age, x, y, directionH)
            y -= new_crab.height+1
            new_crab.set_y(y)
        elif crabtype == 'sh':
            new_crab = Shrimp.Shrimp(name, age, x, y, directionH)
            y -= new_crab.height+1
            new_crab.set_y(y)
        else:
            print('wrong crabtype input, please try again')
            return False
        if not self.check_if_free(x, y):
            return False
        self.anim.append(new_crab)   # add new crab into list animals
        self.print_animal_on_board(new_crab)   # add new crab on board
        return True



    def check_if_free(self, x, y) -> bool:
        """
        method for checking whether the position is empty before inserting a new animal
        """
        if y < WATERLINE or y > self.aqua_height-1:
            print('The Y: {}, place is not valid! Please try again'.format(y))
            return False

        if x <= 0 or x > self.aqua_width - 1:
            print('The X: {} place is not valid! Please try again'.format(x))
            return False

        for animal in self.anim:
            if x >= animal.x and x <= animal.x + 8 and y >= animal.y and y <= animal.y + 8:
                print('The place is not available! Please try again.')
                return False
            else:
                continue
        return True


    def left(self, a):
        self.delete_animal_from_board(a)
        a.left()
        self.print_animal_on_board(a)
        return


    def right(self, a):
        self.delete_animal_from_board(a)
        a.right()
        self.print_animal_on_board(a)
        return

    def up(self, a):
        self.delete_animal_from_board(a)
        a.up()
        self.print_animal_on_board(a)
        return


    def down(self, a):
        self.delete_animal_from_board(a)
        a.down()
        self.print_animal_on_board(a)
        return


    def next_turn(self):

        """
        Managing a single step
        """
        crab_flags = [0]*len(self.anim)  # array where crab who is collide next step gets 1. 0 otherwise
        for i, animal in enumerate(self.anim):  # we move the animals
            #### Crab ####
            if isinstance(animal, Crab.Crab):
                if animal.get_directionH() == 0: # left
                    self.left(animal)
                else: #right
                    self.right(animal)
                # check if we need to change direction
                if self.is_collision(animal):  # the crab is about to collide
                    # crab is about to collide: need to change direction
                    crab_flags[i] = 1   # flag
                if animal.x == 1 or animal.x + animal.width == self.aqua_width-2:
                    animal.set_directionH(abs(animal.directionH - 1))
                    # reverse the animal
                    self.delete_animal_from_board(animal)
                    self.print_animal_on_board(animal)
            #### Fish ####
            elif isinstance(animal, Fish.Fish):
                if animal.get_directionH() == 0: # left
                    self.left(animal)
                else: #right
                    self.right(animal)
                if animal.get_directionV() == 0: # down
                    self.down(animal)
                else: #right
                    self.up(animal)
                # check if we need to change directions
                if animal.x == 1 or animal.x + animal.width == self.aqua_width-1:  # we out of index in aquarium
                    # change the direction
                    animal.set_directionH(abs(animal.directionH - 1))
                    # reverse the animal
                    self.delete_animal_from_board(animal)
                    self.print_animal_on_board(animal)
                if animal.y == WATERLINE or animal.y + animal.height == self.aqua_height - 4:
                    # change the direction
                    animal.set_directionV(abs(animal.directionV - 1))

        for i, animal in enumerate(self.anim):
            if crab_flags[i] == 1:  # need to change direction
                animal.set_directionH(abs(animal.directionH - 1))  # Absolute value of (x-1) : x=0->1 / x=1->0
                self.delete_animal_from_board(animal)   # rewrite the crab with the correct direction
                self.print_animal_on_board(animal)
        if self.turn % 10 == 0:
            for animal in self.anim:
                animal.dec_food()   # decrease in 1 the amount of food every 10 turns
        if self.turn % 100 == 0:
            for animal in self.anim:
                animal.inc_age()
        for animal in self.anim:    # check if animals are dead
            animal_age = animal.get_age()
            animal_food = animal.get_food()
            if animal_age == 120 or animal_food == 0: # animal is dead due happy life or lack of food and luck
                animal.die()
                self.delete_animal_from_board(animal)  # remove animal from board
                self.anim.remove(animal)  # remove animal from list

        self.turn += 1
        return

    def print_all(self):
        """
        Prints all the animals in the aquarium
        """
        for anim in self.anim:
            print(anim)
        return

    def feed_all(self):
        """
        feed all the animals in the aquarium
        """
        for animal in self.anim:
            animal.add_food(10)



    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if animaltype == 'sc' or animaltype == 'mo':
            return self.add_fish(name, age, x, y, directionH, directionV, animaltype)
        elif animaltype == 'oc' or animaltype == 'sh':
            return self.add_crab(name, age, x, y, directionH, animaltype)
            # return True
        else:
            return False

    def several_steps(self) -> None:
        """
        Managing several steps
        """
        steps = int(input())  ###? to add string 'please enter number of steps' etc.?
        for i in range(steps):
            self.next_turn()
        return


