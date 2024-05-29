import random

class GVDie:
    def __init__(self, seed):
        random.seed(seed)
        self._is_heads = True
        self.heads = 0
        self.flips = 0

    def num_flips(self):
        return self.flips

    def num_heads(self):
        return self.heads

    def num_tails(self):
        return self.flips - self.heads

    def flip(self):
        self.is_heads = random.randint(0, 1)
        self.flips += 1
        if self.is_heads == 1:
            self.heads += 1
        else:
            self.heads = 0

    def get_is_heads(self):
        return self.is_heads

    def roll(self):
        self.my_value = self.rand.randint(1,6)

    def to_string(self):
        str = 'Flips', self.flips, 'Heads:', self.heads, 'isHeads', self.is_heads
        return str

    def num_flips(self):
        return self.flips

    def num_heads(self):
        return self.heads

    def num_tails(self):
        return self.flips - self.heads

    def set_to_heads(self, h):
        self.is_heads = h

    def flip_for_tails(gv_coin, goal):
        while gv_coin.num_tails() < goal:
            gv_coin.flip()
        return gv_coin.num_flips()

    def count_heads(gv_coin, goal):
        while gv_coin.num_heads() < goal:
            gv_coin.flip()
        return gv_coin.num_flips()

        # set the random number generator seed for testing

    # allows dice to be compared if necessary
    def set_seed(self, other):
        return self.my_value - d.my_value

def roll_total(die, total):
    rolls = 0
    while total > 0:
        die.roll()
        total -= die.my_value
        rolls += 1
    return rolls

if __name__ == '__main__':
    die = GVDie() # Create a GVDie object
    die.set_seed(15) # Set the GVDie object with seed value 15

    total = int(input())
    rolls = roll_total(die, total) # Should return the number of tolsl to reach total.
    print(f'Number of rolls to reach at least {total}: {rolls}')