import time
import Aqua

def demo(myaqua):
    """
    Running a demo aquarium
    for example:
    myaqua.add_animal("scalarfish1", 4, 10, 10, 1, 0, 'sc')
    myaqua.add_animal("molyfish2", 12, 35, 15, 0, 1, 'mo')
    myaqua.add_animal("shrimpcrab1", 3, 20, myaqua.aqua_height, 1, 0, 'sh')
    myaqua.add_animal("ocypodecrab2", 13, 41, myaqua.aqua_height, 0, 0, 'oc')
    myaqua.print_board()

    for i in range(120):
        ....
    """
    if not myaqua.add_animal("scalarfish1", 4, 10, 10, 1, 0, 'sc'):
        print('failed adding scalar')
    if not myaqua.add_animal("molyfish2", 12, 35, 15, 0, 1, 'mo'):
        print('failed adding moly')
    if not myaqua.add_animal("shrimpcrab1", 3, 20, myaqua.aqua_height, 1, 0, 'sh'):
        print('failed adding shrimp')
    if not myaqua.add_animal("ocypodecrab2", 13, 3, myaqua.aqua_height, 0, 0, 'oc'):
        print('failed adding ocypode')
    myaqua.print_board()

    for i in range(120):
        myaqua.next_turn()
        time.sleep(0.5)
        myaqua.print_board()
        if i % 40 == 0:
            myaqua.feed_all()


def add_animal(myaqua):
    choice = 0
    while not 1 <= choice <= 4:
        print("Please select:")
        print("1. Scalare")
        print("2. Moly")
        print("3. Ocypode")
        print("4. Shrimp")
        choice = int(input("What animal do you want to put in the aquarium?"))

    name = input("Please enter a name:")
    age = 0
    while not 1 <= age <= 100:
        age = int(input("Please enter age:"))

    success = False
    while not success:
        x, y = 0, 0
        while not 1 <= x <= (myaqua.aqua_width - 1):
            x = int(input("Please enter an X axis location (1 - %d):" % (myaqua.aqua_width - 1)))
        if choice == 1 or choice == 2:
            while not Aqua.WATERLINE <= y <= (myaqua.aqua_height - 1):
                y = int(input("Please enter an Y axis location (%d - %d):" % (Aqua.WATERLINE, myaqua.aqua_height - 1)))

        directionH, directionV = -1, -1
        while not (directionH == 0 or directionH == 1):
            directionH = int(input("Please enter horizontal direction (0 for Left, 1 for Right):"))
        if choice == 1 or choice == 2:
            while not (directionV == 0 or directionV == 1):
                directionV = int(input("Please enter vertical direction  (0 for Down, 1 for Up):"))

        if choice == 1:
            success = myaqua.add_animal(name, age, x, y, directionH, directionV, 'sc')
        elif choice == 2:
            success = myaqua.add_animal(name, age, x, y, directionH, directionV, 'mo')
        elif choice == 3:
            success = myaqua.add_animal(name, age, x, myaqua.aqua_height, directionH, 0, 'oc')
        else:
            success = myaqua.add_animal(name, age, x, myaqua.aqua_height, directionH, 0, 'sh')
    return None


if __name__ == '__main__':
    width = 0
    height = 0

    print('Welcome to "The OOP Aquarium"')
    while width < 40:
        width = int(input("The width of the aquarium (Minimum 40): "))
    while height < 25:
        height = int(input("The height of the aquarium (Minimum 25): "))
    myaqua = Aqua.Aqua(width, height)   # initialize a new Aqua class object

    while True:
        choice = 0  # will hold the command number that the user choose
        while not 1 <= choice <= 7:
            print("Main menu")
            print("-" * 30)
            print("1. Add an animal")
            print("2. Drop food into the aquarium")
            print("3. Take a step forward")
            print("4. Take several steps")
            print("5. Demo")
            print("6. Print all")
            print("7. Exit")

            choice = int(input("What do you want to do?"))

        if choice == 1:
            add_animal(myaqua)
        elif choice == 2:
            myaqua.feed_all()
        elif choice == 3:
            myaqua.next_turn()
        elif choice == 4:
            myaqua.several_steps()
        elif choice == 5:
            demo(myaqua)
        elif choice == 6:
            myaqua.print_all()
        else:
            print("Bye bye")
            exit()

        myaqua.print_board()
