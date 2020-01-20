#!/usr/bin/env python3

from random import *
import argparse

from character import character
from character import cfg

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
parser.add_argument("-2", "--2up",
                        help="Format for 2 per page, landscape",
                        action="store_true",
                        default=False,
                        dest="_2up"
                        )
parser.add_argument("-r", "--random",
                        help="Roll a random class",
                        action="store_true",
                        default=False,
                        dest="random_class"
                        )
parser.add_argument("-d", "--dice",
                        help="Number of dice to roll to get stats; will pick best 3",
                        action="store",
                        default=4,
                        type=int,
                        dest="dice"
                        )
args = parser.parse_args()
cfg.character_class = args.character_class
cfg.min_attribute_value = args.min_attribute_value
cfg._2up = args._2up
cfg.random_class = args.random_class
cfg.dice = args.dice if args.dice >= 3 else 3

allowed_classes = cfg.allowed_classes
character_class = cfg.character_class
min_attribute_value = cfg.min_attribute_value
_2up = cfg._2up
random_class = cfg.random_class
dice = cfg.dice

if character_class not in allowed_classes:
    args = parser.parse_args(['-h'])
    exit()

if random_class:
    from random import *
    pick = randint( 0, 3 )
    character_class = allowed_classes[pick]
# == End Init == #

def main():
    new_character = character.Character(character_class)
    print(f"{new_character}")

    str_bonus = ""
    int_bonus = ""
    wis_bonus = ""
    dex_bonus = ""
    con_bonus = ""
    cha_bonus = ""
    if new_character.attributes['str'].skill_bonus() != 0:
        str_bonus = new_character.attributes['str'].bonus_strings['str'].format(
            new_character.attributes['str'].skill_bonus(),
            new_character.attributes['str'].skill_bonus(),
            new_character.attributes['str'].xp_bonus()*100
            )

    if new_character.attributes['int'].skill_bonus() != 0:
        int_bonus = new_character.attributes['int'].bonus_strings['int'].format(
            new_character.attributes['int'].skill_bonus(),
            new_character.attributes['int'].xp_bonus()*100
            )

    if new_character.attributes['wis'].skill_bonus() != 0:
        wis_bonus = new_character.attributes['wis'].bonus_strings['wis'].format(
            new_character.attributes['wis'].skill_bonus(),
            new_character.attributes['wis'].xp_bonus()*100
            )

    if new_character.attributes['dex'].skill_bonus() != 0:
        dex_bonus = new_character.attributes['dex'].bonus_strings['dex'].format(
            new_character.attributes['dex'].skill_bonus(),
            new_character.attributes['dex'].skill_bonus(),
            new_character.attributes['dex'].xp_bonus()*100
            )

    if new_character.attributes['con'].skill_bonus() != 0:
        con_bonus = new_character.attributes['con'].bonus_strings['con'].format(
            new_character.attributes['con'].skill_bonus()
            )

    if new_character.attributes['cha'].skill_bonus() != 0:
        cha_bonus = new_character.attributes['cha'].bonus_strings['cha'].format(
            new_character.attributes['cha'].skill_bonus()
            )

    print("+==================================================================+".format())
    print("|                                |   Money     |      Sketch       |".format())
    print("| Name:__________________________|             |                   |".format())
    print("|                                |             |                   |".format())
    print("| Player:________________________|PP:___GP:___ |                   |".format())
    print("|                                |             |                   |".format())
    print("| Class: {:<23} |EP:___SP:___ |                   |".format(new_character.character_class.name.upper()))
    print("|                                |             |                   |".format())
    print("| Alignment:_____________________|CP:___       |                   |".format())
    print("|                                |             |                   |".format())
    print("| LVL:________ AC:______ Sex:____|OTHER:       |                   |".format())
    print("|                                |             |                   |".format())
    print("| HP:______ XP:______ Dmg:_______|____________ |                   |".format())
    print("|                                              |                   |".format())
    print("|                                     Saving   |                   |".format())
    print("| Attribs   Modifiers                 Throws   |                   |".format())
    print("|     +--+  +-----------------------+ Poison+--|-- Weapons/Armor --|".format())
    print("| STR:|{:>2}|  |{:<23}| Death |  |                   |".format(new_character.attributes['str'].value,str_bonus))
    print("|     +--+  +-----------------------+ Ray   +--|                  |".format())
    print("|     +--+  +-----------------------+          |                   |".format())
    print("| INT:|{:>2}|  |{:23}| Magic +--|                   |".format(new_character.attributes['int'].value,int_bonus))
    print("|     +--+  +-----------------------+ Wand  |  |                   |".format())
    print("|     +--+  +-----------------------+       +--|                   |".format())
    print("| WIS:|{:>2}|  |{:23}|          |                   |".format(new_character.attributes['wis'].value,wis_bonus))
    print("|     +--+  +-----------------------+ Stone/+--|                   |".format())
    print("|     +--+  +-----------------------+ Paral-|  |-- Normal Items ---|".format())
    print("| DEX:|{:>2}|  |{:23}| ysis  +--|                   |".format(new_character.attributes['dex'].value,dex_bonus))
    print("|     +--+  +-----------------------+          |                   |".format())
    print("|     +--+  +-----------------------+ Dragon+--|                   |".format())
    print("| CON:|{:>2}|  |{:23}| Breath|  |                   |".format(new_character.attributes['con'].value,con_bonus))
    print("|     +--+  +-----------------------+       +--|                   |".format())
    print("|     +--+  +-----------------------+          |                   |".format())
    print("| CHA:|{:>2}|  |{:23}| Spell +--|                   |".format(new_character.attributes['cha'].value,cha_bonus))
    print("|     +--+  +-----------------------+ Magic |  |                   |".format())
    print("| Languages:_________________________ Staff +--|-- Magic Items ----|".format())
    print("+-To Hit AC------------------------------------|                   |".format())
    print("|  9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | -1  |                   |".format())
    print("+----------------------------------------------|                   |".format())
    print("|    |   |   |   |   |   |   |   |   |   |     |                   |".format())
    print("+----+---+---+---+---+---+---+---+---+---+-----|-- Other ----------|".format())
    if character_class in ('thief','cleric'):
        print("|-- {:-<43}|                   |".format(character_class.title()+" Skills "))
    else:
        print("|-- Notes -------------------------------------|                   |".format())
    print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    if character_class in ('wizard','cleric'):
        print("|-- Spells ------------------------------------|                   |".format())
    elif character_class in ('thief'):
        print("|-- Notes -------------------------------------|                   |".format())
    else:
        print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    if _2up:
        print("|                                              |                   |".format())
        print("|                                              |                   |".format())
        print("|                                              |                   |".format())
    print("+==================================================================+".format())

##################################
if __name__ == "__main__":
    main()
