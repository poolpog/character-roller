#!/usr/bin/env python

from random import *
import argparse

parser = argparse.ArgumentParser()  
parser.add_argument("-c", "--class",
                        help="Character class. One of: fighter, thief, wizard, cleric. Defaults to 'fighter'",
                        action="store",
                        default="fighter",
                        dest="character_class"
                        )
parser.add_argument("-m", "--min-attribute-value",
                        help="Minimum primary attribute value for character class. Defaults to '15'",
                        action="store",
                        type=int,
                        default=15,
                        dest="min_attribute_value"
                        )
parser.add_argument("-2", "--2up",
                        help="Format for 2 per page, landscape",
                        action="store_true",
                        default=False,
                        dest="_2up"
                        )
args = parser.parse_args()  
character_class = args.character_class
min_attribute_value = args.min_attribute_value
_2up = args._2up

if character_class not in ( "fighter", "thief", "wizard", "cleric" ):
    args = parser.parse_args(['-h'])  
    exit()

class Character():
    attributes = ""
    global min_attribute_value

    def __init__(self, character_class = ""):
        self.attributes = {
            'strength':3,
            'intelligence':3,
            'wisdom':3,
            'dexterity':3,
            'constitution':3,
            'charisma':3
            }

        self.character_class     = CharacterClass(character_class)
        primary_attributes =  self.character_class.primary_attribute_map[character_class]

        self.attributes['strength']     = Attribute()
        self.attributes['intelligence'] = Attribute()
        self.attributes['wisdom']       = Attribute()
        self.attributes['dexterity']    = Attribute()
        self.attributes['constitution'] = Attribute()
        self.attributes['charisma']     = Attribute()

        for attribute in primary_attributes:
            while self.attributes[attribute].value < min_attribute_value:
                self.attributes[attribute] = Attribute()


class CharacterClass():
    name = ""
    primary_attribute_map = {
        'fighter': ['strength'],
        'wizard': ['intelligence'],
        'cleric': ['wisdom'],
        'thief': ['dexterity'],
        'dwarf': ['strength','constitution'],
        'elf': ['strength','intelligence'],
        'halfling': ['strength','dexterity']
    }

    def __init__(self,name):
        self.name = name

    def get_primary_attributes():
        return primary_attribute_map[name]

    def get_name():
        return name

class Attribute():
    value = 0
    bonus_strings = {
        'strength':     '{:>+2d} melee,{:>+2d} dmg,{:>+3.0f}% xp',
        'intelligence': '{:>+2d} languages,{:>+3.0f}% xp',
        'wisdom':       '{:>+2d} save v spell,{:>+3.0f}% xp',
        'dexterity':    '{:>+2d} missle,{:>+2d} AC,{:>+3.0f}% xp',
        'constitution': '{:>+2d} HP',
        'charisma':     '{:>+2d} NPC react'
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

class HitPoints():
    value = 1
    d_dict = {
        'fighter': 8,
        'thief': 4,
        'magicuser': 4,
        'cleric': 6,
        'elf': 6,
        'dwarf': 8,
        'halfling': 6,
        'mystic': 6,
    }


def main():
    new_character = Character(character_class)

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
            new_character.attributes['constitution'].skill_bonus()
            )

    if new_character.attributes['charisma'].skill_bonus() != 0:
        charisma_bonus = new_character.attributes['charisma'].bonus_strings['charisma'].format(
            new_character.attributes['charisma'].skill_bonus()
            )

    print "+==================================================================+".format()
    print "|                                |   Money     |      Sketch       |".format()
    print "| Name:__________________________|             |                   |".format()
    print "|                                |             |                   |".format()
    print "| Player:________________________|PP:___GP:___ |                   |".format()
    print "|                                |             |                   |".format()
    print "| Class: {:<23} |EP:___SP:___ |                   |"\
            .format(new_character.character_class.name.upper())
    print "|                                |             |                   |".format()
    print "| Alignment:_____________________|CP:___       |                   |".format()
    print "|                                |             |                   |".format()
    print "| LVL:________ AC:______ Sex:____|OTHER:       |                   |".format()
    print "|                                |             |                   |".format()
    print "| HP:______ XP:______ Dmg:_______|____________ |                   |".format()
    print "|                                              |                   |".format()
    print "|                                     Saving   |                   |".format()
    print "| Attribs   Modifiers                 Throws   |                   |".format()
    print "|     +--+  +-----------------------+ Poison+--|-- Weapons/Armor --|".format()
    print "| STR:|{:>2}|  |{:<23}| Death |  |                   |"\
            .format(new_character.attributes['strength'].value,strength_bonus)
    print "|     +--+  +-----------------------+ Ray   +--|                   |".format()
    print "|     +--+  +-----------------------+          |                   |".format()
    print "| INT:|{:>2}|  |{:23}| Magic +--|                   |"\
            .format(new_character.attributes['intelligence'].value,intelligence_bonus)
    print "|     +--+  +-----------------------+ Wand  |  |                   |".format()
    print "|     +--+  +-----------------------+       +--|                   |".format()
    print "| WIS:|{:>2}|  |{:23}|          |                   |"\
            .format(new_character.attributes['wisdom'].value,wisdom_bonus)
    print "|     +--+  +-----------------------+ Stone/+--|                   |".format()
    print "|     +--+  +-----------------------+ Paral-|  |-- Normal Items ---|".format()
    print "| DEX:|{:>2}|  |{:23}| ysis  +--|                   |"\
            .format(new_character.attributes['dexterity'].value,dexterity_bonus)
    print "|     +--+  +-----------------------+          |                   |".format()
    print "|     +--+  +-----------------------+ Dragon+--|                   |".format()
    print "| CON:|{:>2}|  |{:23}| Breath|  |                   |"\
            .format(new_character.attributes['constitution'].value,constitution_bonus)
    print "|     +--+  +-----------------------+       +--|                   |".format()
    print "|     +--+  +-----------------------+          |                   |".format()
    print "| CHA:|{:>2}|  |{:23}| Spell +--|                   |"\
            .format(new_character.attributes['charisma'].value,charisma_bonus)
    print "|     +--+  +-----------------------+ Magic |  |                   |".format()
    print "| Languages:_________________________ Staff +--|-- Magic Items ----|".format()
    print "| Cleric or Thief Skills:                      |                   |".format()
    print "|                                              |                   |".format()
    print "|                                              |                   |".format()
    print "|                                              |                   |".format()
    print "+-To Hit AC------------------------------------|                   |".format()
    print "|  9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | -1  |                   |".format()
    print "+----------------------------------------------|                   |".format()
    print "|    |   |   |   |   |   |   |   |   |   |     |                   |".format()
    print "+----+---+---+---+---+---+---+---+---+---+-----|-- Other ----------|".format()
    print "| Notes                                        |                   |".format()
    print "|                                              |                   |".format()
    print "|                                              |                   |".format()
    print "|                                              |                   |".format()
    print "|                                              |                   |".format()
    print "|                                              |                   |".format()
    if _2up:
        print "|                                              |                   |".format()
        print "|                                              |                   |".format()
        print "|                                              |                   |".format()
    print "+==================================================================+".format()

##################################
if __name__ == "__main__":
    main()
