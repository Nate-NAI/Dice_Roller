"""
This program is intended to determine results of a d100 for Call of Cthulhu
and other BRP RPGs.
"""

__author__ = "Nathan Winslow"
__copyright__ = "MIT"

import random

random.seed()


def get_fumble(skill_val):
    return 100 if skill_val >= 50 else 96


class Die(object):

    def __init__(self, skill_val=42):
        self.fumble = get_fumble(skill_val)
        self.skill_val = skill_val
        self.hard_suc = round(skill_val / 2)
        self.extreme_suc = round(skill_val / 5)
        self.last_result = 0

    def __call__(self, bonus=0, penalty=0):

        modifier = abs(bonus - penalty)

        if modifier != 0:

            ones_digit = random.randint(0, 9)
            tens_digit = [random.randint(0, 9) * 10]

            i = 0
            while i < modifier:
                tens_digit.append(random.randint(0, 9) * 10)
                i += 1

            tens_digit.sort()
            high = 0

            if bonus > penalty:
                high = tens_digit[0]

            elif penalty > bonus:
                high = tens_digit[i]

            result = high + ones_digit

        else:
            result = random.randint(1, 100)

        if result == 0:  # interpret the result according to the game
            result = 100

        self.last_result = result
        return result


# Test Code #
if __name__ == "main":
    skill = 75
    roller = Die(skill)
    try:
        running = True
        while running:
            val = roller()
            print(val)
            x = input("would you like to roll again? Y/n")
            if x == 'n' or x == 'N':
                running = False
    except KeyboardInterrupt:
        print("shutting down...")