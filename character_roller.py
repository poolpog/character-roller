#!/usr/bin/env python3
# TODO
#   * use json as default output format
#   * use json output to populate different other output formats
#   * add OutputFormat as a class?
#   * update to use D&D 5e rules for character gen

from __future__ import print_function

from random import *
import argparse

# == Init == #
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
parser.add_argument("-r", "--random",
                        help="Roll a random class",
                        action="store_true",
                        default=False,
                        dest="random_class"
                        )
parser.add_argument("-f", "--output_format",
                        help="Output format",
                        action="store",
                        default="text",
                        dest="output_format"
                        )
parser.add_argument("-d", "--dice",
                        help="Number of dice to roll to get stats; will pick best 3",
                        action="store",
                        default=4,
                        type=int,
                        dest="dice"
                        )
args = parser.parse_args()  
character_class = args.character_class
output_format = args.output_format
min_attribute_value = args.min_attribute_value
random_class = args.random_class
dice = args.dice if args.dice >= 3 else 3
allowed_classes = ( "fighter", "thief", "wizard", "cleric" )
allowed_output_formats = ( "text", "json", "html" )

if character_class not in allowed_classes:
    args = parser.parse_args(['-h'])  
    exit()

if output_format not in allowed_output_formats:
    output_format = "text"

if random_class:
    from random import *
    pick = randint( 0, 3 )
    character_class = allowed_classes[pick]

# == End Init == #

# == Class Defs == #
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
        global dice
        rolls = []
        for i in range(dice):
            rolls.append(randint(1,6))
        for i in range(dice - 3):
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


def main(output_format=output_format):
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

    output = ""
    if output_format == "text":
        output += "+==================================================================+\n".format()
        output += "|                                |   Money     |      Sketch       |\n".format()
        output += "| Name:__________________________|             |                   |\n".format()
        output += "|                                |             |                   |\n".format()
        output += "| Player:________________________|PP:___GP:___ |                   |\n".format()
        output += "|                                |             |                   |\n".format()
        output += "| Class: {:<23} |EP:___SP:___ |                   |\n"\
                .format(new_character.character_class.name.upper())
        output += "|                                |             |                   |\n".format()
        output += "| Alignment:_____________________|CP:___       |                   |\n".format()
        output += "|                                |             |                   |\n".format()
        output += "| LVL:________ AC:______ Sex:____|OTHER:       |                   |\n".format()
        output += "|                                |             |                   |\n".format()
        output += "| HP:______ XP:______ Dmg:_______|____________ |                   |\n".format()
        output += "|                                              |                   |\n".format()
        output += "|                                     Saving   |                   |\n".format()
        output += "| Attribs   Modifiers                 Throws   |                   |\n".format()
        output += "|     +--+  +-----------------------+ Poison+--|-- Weapons/Armor --|\n".format()
        output += "| STR:|{:>2}|  |{:<23}| Death |  |                   |\n"\
                .format(new_character.attributes['strength'].value,strength_bonus)
        output += "|     +--+  +-----------------------+ Ray   +--|                   |\n".format()
        output += "|     +--+  +-----------------------+          |                   |\n".format()
        output += "| INT:|{:>2}|  |{:23}| Magic +--|                   |\n"\
                .format(new_character.attributes['intelligence'].value,intelligence_bonus)
        output += "|     +--+  +-----------------------+ Wand  |  |                   |\n".format()
        output += "|     +--+  +-----------------------+       +--|                   |\n".format()
        output += "| WIS:|{:>2}|  |{:23}|          |                   |\n"\
                .format(new_character.attributes['wisdom'].value,wisdom_bonus)
        output += "|     +--+  +-----------------------+ Stone/+--|                   |\n".format()
        output += "|     +--+  +-----------------------+ Paral-|  |-- Normal Items ---|\n".format()
        output += "| DEX:|{:>2}|  |{:23}| ysis  +--|                   |\n"\
                .format(new_character.attributes['dexterity'].value,dexterity_bonus)
        output += "|     +--+  +-----------------------+          |                   |\n".format()
        output += "|     +--+  +-----------------------+ Dragon+--|                   |\n".format()
        output += "| CON:|{:>2}|  |{:23}| Breath|  |                   |\n"\
                .format(new_character.attributes['constitution'].value,constitution_bonus)
        output += "|     +--+  +-----------------------+       +--|                   |\n".format()
        output += "|     +--+  +-----------------------+          |                   |\n".format()
        output += "| CHA:|{:>2}|  |{:23}| Spell +--|                   |\n"\
                .format(new_character.attributes['charisma'].value,charisma_bonus)
        output += "|     +--+  +-----------------------+ Magic |  |                   |\n".format()
        output += "| Languages:_________________________ Staff +--|-- Magic Items ----|\n".format()
        output += "+-To Hit AC------------------------------------|                   |\n".format()
        output += "|  9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | -1  |                   |\n".format()
        output += "+----------------------------------------------|                   |\n".format()
        output += "|    |   |   |   |   |   |   |   |   |   |     |                   |\n".format()
        output += "+----+---+---+---+---+---+---+---+---+---+-----|-- Other ----------|\n".format()
        if character_class in ('thief','cleric'):
            output += "|-- {:-<43}|                   |\n".format(character_class.title()+" Skills ")
        else:
            output += "|-- Notes -------------------------------------|                   |\n".format()
        output += "|                                              |                   |\n".format()
        output += "|                                              |                   |\n".format()
        output += "|                                              |                   |\n".format()
        output += "|                                              |                   |\n".format()
        if character_class in ('wizard','cleric'):
            output += "|-- Spells ------------------------------------|                   |\n".format()
        elif character_class in ('thief'):
            output += "|-- Notes -------------------------------------|                   |\n".format()
        else:
            output += "|                                              |                   |\n".format()
        output += "|                                              |                   |\n".format()
        output += "|                                              |                   |\n".format()
        output += "|                                              |                   |\n".format()
        output += "|                                              |                   |\n".format()
        output += "+==================================================================+\n".format()

    elif output_format == "json":
        output = '{'
        output += '"class": "{}",'.format(new_character.character_class.name.upper())
        output += '"str": "{}", "str_bonus": "{}",'.format(new_character.attributes['strength'].value,strength_bonus)
        output += '"int": "{}", "int_bonus": "{}",'.format(new_character.attributes['intelligence'].value,intelligence_bonus)
        output += '"wis": "{}", "wis_bonus": "{}",'.format(new_character.attributes['wisdom'].value,wisdom_bonus)
        output += '"dex": "{}", "dex_bonus": "{}",'.format(new_character.attributes['dexterity'].value,dexterity_bonus)
        output += '"con": "{}", "con_bonus": "{}",'.format(new_character.attributes['constitution'].value,constitution_bonus)
        output += '"cha": "{}", "cha_bonus": "{}"'.format(new_character.attributes['charisma'].value,charisma_bonus)
        output += '}\n'
    
    return output

##################################
if __name__ == "__main__":
    output = main()
    print(output)
