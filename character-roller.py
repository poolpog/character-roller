#!/usr/bin/env python

from random import *

class Character():
    attributes = ""

    def __init__(self):
        self.attributes = {
            'strength':3,
            'intelligence':3,
            'wisdom':3,
            'dexterity':3,
            'constitution':3,
            'charisma':3
            }

        self.attributes['strength']     = Attribute()
        self.attributes['intelligence'] = Attribute()
        self.attributes['wisdom']       = Attribute()
        self.attributes['dexterity']    = Attribute()
        self.attributes['constitution'] = Attribute()
        self.attributes['charisma']     = Attribute()

class Attribute():
    value = 0

    def __init__(self):
        self.roll()

    def roll(self):
        rolls = [
            randint(1,6),
            randint(1,6),
            randint(1,6),
            randint(1,6)
            ]
        for i in range(0,1):
            min_value = min(rolls)
            min_index = rolls.index(min_value)
            del rolls[min_index]
        self.value = sum(rolls)

    def skill_bonus(self):
        out = 0
        if self.value > 1 and self.value <= 3:
            out = -3
        elif self.value >= 4 and self.value <= 5:
            out = -2
        elif self.value >= 6 and self.value <= 8:
            out = -1
        elif self.value >= 9 and self.value <= 12:
            out = 0
        elif self.value >= 13 and self.value <= 15:
            out = +1
        elif self.value >= 16 and self.value <= 17:
            out = +2
        elif self.value == 18:
            out = +3
        return out

    def xp_bonus(self):
        out = 0
        if self.value > 1 and self.value <= 5:
            out = -.2
        elif self.value >= 6 and self.value <= 8:
            out = -.1
        elif self.value >= 13 and self.value <= 15:
            out = +.05
        elif self.value >= 16 and self.value <= 18:
            out = +.10
        return out

def main():
    new_character = Character()

    attribute_names = [ "strength", "intelligence", "wisdom", "dexterity", "constitution", "charisma" ]

    for name in attribute_names:
        print "{:>13} => {:2}".format( name.title(), new_character.attributes[name].value)
        print "{:>30} => {:>+3d}".format( (name + " bonus").title(), new_character.attributes[name].skill_bonus())
        print "{:>30} => {:>+3.0f}%".format( (name + " XP bonus").title(), ( new_character.attributes[name].xp_bonus() *100 ))


##################################
if __name__ == "__main__":
    main()
