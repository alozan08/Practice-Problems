import random


class GVDie:
    def __init__(self):
        # set default values
        self.my_value = random.randint(1, 6)
        self.rand = random.Random()

    def roll(self):
        self.my_value = self.rand.randint(1, 6)

        # set the random number generator seed for testing

    def set_seed(self, seed):
        self.rand.seed(seed)

    # allows dice to be compared if necessary
    def compare_to(self, other):
        return self.my_value - d.my_value


def roll_specific_number(die, num, goal):
    count_x = 0
    count_y = 0

    while count_y < goal:
        die.roll()
        if die.my_value == num:
            count_y += 1
        count_x += 1
    return count_x


# Type your code here

if __name__ == "__main__":
    die = GVDie()  # Create a GVDie object
    die.set_seed(15)  # Set the GVDie object with seed value 15

    num = int(input())
    goal = int(input())
    rolls = roll_specific_number(die, num, goal)  # Call roll_specific_number() and return number of rolls.
    print(f'It took {rolls} rolls to get a \"{num}\" {goal} times.')
