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
        self.attributes['strength']     = self.roll_attribute()
        self.attributes['intelligence'] = self.roll_attribute()
        self.attributes['wisdom']       = self.roll_attribute()
        self.attributes['dexterity']    = self.roll_attribute()
        self.attributes['constitution'] = self.roll_attribute()
        self.attributes['charisma']     = self.roll_attribute()

    def roll_attribute(self):
        self.attribute = [
            randint(1,6),
            randint(1,6),
            randint(1,6),
            randint(1,6)
            ]
        for i in range(0,1):
            min_value = min(self.attribute)
            min_index = self.attribute.index(min_value)
            del self.attribute[min_index]

        return sum(self.attribute)

new_character = Character()
for attribute in new_character.attributes:
    print "%s = %d" % ( attribute, new_character.attributes[attribute] )
