from random import *

from character.cfg import Cfg

class HitPoints():
    def __init__(self, config):
        self.config = config
        self.value = 0
        self.d_dict = {
                'fighter': 8,
                'thief': 4,
                'magicuser': 4,
                'cleric': 6
            }
        self.roll()

    def roll(self):
        rolls = []
        for i in range(self.config.level):
            rolls.append(randint(1,self.d_dict[self.config.character_class]))
        self.value = sum(rolls)

class HitPoints5e():
    def __init__(self, config):
        self.value = 0
        self.d_dict = {
                'barbarian': 12,
                'bard': 8,
                'cleric': 8,
                'druid': 8,
                'fighter': 10,
                'monk': 8,
                'paladin': 10,
                'ranger': 10,
                'rogue': 8,
                'sorcerer': 6,
                'thief': 8,
                'warlock': 8,
                'wizard': 6,
            }
        self.roll()

class HitPointsBasic():
    def __init__(self, config):
        self.config = config
        self.value = 0
        self.d_dict = {
                'fighter': 8,
                'thief': 4,
                'magicuser': 4,
                'cleric': 6,
                'elf': 6,
                'dwarf': 8,
                'halfling': 6,
                'mystic': 6,
            }
        self.roll()
