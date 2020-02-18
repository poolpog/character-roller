#!/usr/bin/env python3

from random import *

from character.character import Character
from character.cfg import Cfg

# == Init == #
config = Cfg()

# == End Init == #

def main():
    new_character = Character(config)

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
    print("| HP:{:>2}  XP:______ Dmg:_______|____________ |                   |".format(new_character.bonus_modified['hp']))
    print("|                                              |                   |".format())
    print("|                                     Saving   |                   |".format())
    print("| Attribs   Modifiers                 Throws   |                   |".format())
    print("|     +--+  +-----------------------+ Poison+--|-- Weapons/Armor --|".format())
    print("| STR:|{:>2}|  |{:<23}| Death |  |                   |".format(new_character.attributes['str'].value,str_bonus))
    print("|     +--+  +-----------------------+ Ray   +--|                   |".format())
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
    if new_character.character_class in ['thief','cleric']:
        print("|-- {:-<43}|                   |".format(new_character.character_class.title()+" Skills "))
    else:
        print("|-- Notes -------------------------------------|                   |".format())
    print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    if new_character.character_class in ['wizard','cleric']:
        print("|-- Spells ------------------------------------|                   |".format())
    elif new_character.character_class in ['thief']:
        print("|-- Notes -------------------------------------|                   |".format())
    else:
        print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    print("|                                              |                   |".format())
    print("+==================================================================+".format())

##################################
if __name__ == "__main__":
    main()
