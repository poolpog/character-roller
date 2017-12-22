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
    bonus_strings = {
        #               '122345678901234567890123'
        'strength':     '{:>+2d}melee,{:>+2d}dmg,{:>+3.0f}% xp',
        #'strength':     '@@ melee,@@@ dmg,@@@% xp',
        #               
        'intelligence': '{:>+2d} languages,{:>+3.0f}% xp',
        'wisdom':       '{:>+2d} save v spell,{:>+3.0f}% xp',
        'dexterity':    '{:>+2d} missle,{:>+2d} AC,{:>+3.0f}% xp',
        'constitution': '{:>+2d} HP,{:>+3.0f}% xp',
        'charisma':     '{:>+2d} NPC react,{:>+3.0f}% xp'
    }

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
        #print "{:>13} => {:2}".format( name.title(), new_character.attributes[name].value)
        #print "{:>30} => {:>+3d}".format( (name + " bonus").title(), new_character.attributes[name].skill_bonus())
        #print "{:>30} => {:>+3.0f}%".format( (name + " XP bonus").title(), ( new_character.attributes[name].xp_bonus() *100 ))
        print "{:>13} => {:2}".format( name.title(), new_character.attributes[name].value)
        print "{:>30} => {:>3}".format( (name + " bonus").title(), new_character.attributes[name].skill_bonus())
        print "{:>30} => {:>3}%".format( (name + " XP bonus").title(), ( new_character.attributes[name].xp_bonus() *100 ))

    strength_bonus = ""
    intelligence_bonus = ""
    wisdom_bonus = ""
    dexterity_bonus = ""
    constitution_bonus = ""
    charisma_bonus = ""
    if new_character.attributes['strength'].skill_bonus() != 0:
        strength_bonus = new_character.attributes['strength'].bonus_strings['strength'].format(
            new_character.attributes['strength'].skill_bonus(),
            new_character.attributes['strength'].skill_bonus(),
            new_character.attributes['strength'].xp_bonus()*100
            )

    if new_character.attributes['intelligence'].skill_bonus() != 0:
        intelligence_bonus = new_character.attributes['intelligence'].bonus_strings['intelligence'].format(
            new_character.attributes['intelligence'].skill_bonus(),
            new_character.attributes['intelligence'].xp_bonus()*100
            )

    if new_character.attributes['wisdom'].skill_bonus() != 0:
        wisdom_bonus = new_character.attributes['wisdom'].bonus_strings['wisdom'].format(
            new_character.attributes['wisdom'].skill_bonus(),
            new_character.attributes['wisdom'].xp_bonus()*100
            )

    if new_character.attributes['dexterity'].skill_bonus() != 0:
        dexterity_bonus = new_character.attributes['dexterity'].bonus_strings['dexterity'].format(
            new_character.attributes['dexterity'].skill_bonus(),
            new_character.attributes['dexterity'].skill_bonus(),
            new_character.attributes['dexterity'].xp_bonus()*100
            )

    if new_character.attributes['constitution'].skill_bonus() != 0:
        constitution_bonus = new_character.attributes['constitution'].bonus_strings['constitution'].format(
            new_character.attributes['constitution'].skill_bonus(),
            new_character.attributes['constitution'].xp_bonus()*100
            )

    if new_character.attributes['charisma'].skill_bonus() != 0:
        charisma_bonus = new_character.attributes['charisma'].bonus_strings['charisma'].format(
            new_character.attributes['charisma'].skill_bonus(),
            new_character.attributes['charisma'].xp_bonus()*100
            )

    print "+----------------------------------------------+-------------------+".format()
    print "| Character Name:________________|Money        |Sketch             |".format()
    print "|    Player Name:________________|PP:___GP:___ |                   |".format()
    print "| Class:_________________________|EP:___SP:___ |                   |".format()
    print "| Alignment:_____________________|CP:___       |                   |".format()
    print "| LVL:____ HP:____ AC:____ XP:___|OTHER:_____  |                   |".format()
    print "|                                              |                   |".format()
    print "|                                     Saving   |                   |".format()
    print "| Attribs   Modifiers                 Throws   |                   |".format()
    print "|     +--+  +-----------------------+ Poison+--+                   |".format()
    print "| STR:|{:>2}|  |{:<23}| Death |  |                   |".format(new_character.attributes['strength'].value,strength_bonus)
    print "|     +--+  +-----------------------+ Ray   +--+                   |".format()
    print "|     +--+  +-----------------------+          |                   |".format()
    print "| INT:|{:>2}|  |{:23}| Magic +--+                   |".format(new_character.attributes['intelligence'].value,intelligence_bonus)
    print "|     +--+  +-----------------------+ Wand  |  +-- Weapons/Armor --+".format()
    print "|     +--+  +-----------------------+       +--+                   |".format()
    print "| WIS:|{:>2}|  |{:23}|          |                   |".format(new_character.attributes['wisdom'].value,wisdom_bonus)
    print "|     +--+  +-----------------------+ Stone/+--+                   |".format()
    print "|     +--+  +-----------------------+ Paral-+  |                   |".format()
    print "| DEX:|{:>2}|  |{:23}| ysis  +--+                   |".format(new_character.attributes['dexterity'].value,dexterity_bonus)
    print "|     +--+  +-----------------------+          |                   |".format()
    print "|     +--+  +-----------------------+ Dragon+--+                   |".format()
    print "| CON:|{:>2}|  |{:23}| Breath|  |                   |".format(new_character.attributes['constitution'].value,constitution_bonus)
    print "|     +--+  +-----------------------+       +--+-- Normal Items ---|".format()
    print "|     +--+  +-----------------------+          |                   |".format()
    print "| CHA:|{:>2}|  |{:23}| Spell +--+                   |".format(new_character.attributes['charisma'].value,charisma_bonus)
    print "|     +--+  +-----------------------+ Magic |  |                   |".format()
    print "| Languages:_________________________ Staff +--+                   |".format()
    print "| Cleric or Thief Skills:                      |                   |".format()
    print "|                                              |                   |".format()
    print "+-To Hit AC------------------------------------+                   |".format()
    print "|  9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | -1  |                   |".format()
    print "+----------------------------------------------+-- Magic Items ----|".format()
    print "|    |   |   |   |   |   |   |   |   |   |     |                   |".format()
    print "+----+---+---+---+---+---+---+---+---+---+-----+                   |".format()
    print "| Notes                                        |                   |".format()
    print "|                                              |                   |".format()
    print "|                                              |                   |".format()
    print "|                                              |                   |".format()
    print "+----------------------------------------------+-------------------+".format()



##################################
if __name__ == "__main__":
    main()
