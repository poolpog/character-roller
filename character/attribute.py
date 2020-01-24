from random import *

from character.cfg import Cfg

# Implementation
class Attribute():
    value = 0
    name = ""
    bonus_strings = {
        'str': '',
        'int': '',
        'wis': '',
        'dex': '',
        'con': '',
        'cha': '',
    }

    def __init__(self, config):
        self.config = config

    def roll(self):
        rolls = []
        for i in range(self.config.dice):
            rolls.append(randint(1,6))
        for i in range(self.config.dice - 3):
            min_value = min(rolls)
            min_index = rolls.index(min_value)
            del rolls[min_index]
        self.value = sum(rolls)


    def skill_bonus(self):
        return 0

    def xp_bonus(self):
        return 0

# 
class Attribute5e(Attribute):
    bonus_strings = {
        'str': '{:>+2d}',
        'int': '{:>+2d}',
        'wis': '{:>+2d}',
        'dex': '{:>+2d}',
        'con': '{:>+2d}',
        'cha': '{:>+2d}'
    }

    def __init__(self, config):
        self.config = config
        self.roll()

    def skill_bonus(self):
        return (self.value-10)//2

    def xp_bonus(self):
        return self.skill_bonus()

class AttributeBasic(Attribute):
    value = 0
    bonus_strings = {
        'str': '{:>+2d} melee,{:>+2d} dmg,{:>+3.0f}% xp',
        'int': '{:>+2d} languages,{:>+3.0f}% xp',
        'wis': '{:>+2d} save v spell,{:>+3.0f}% xp',
        'dex': '{:>+2d} missle,{:>+2d} AC,{:>+3.0f}% xp',
        'con': '{:>+2d} HP',
        'cha': '{:>+2d} NPC react'
    }

    def __init__(self, config):
        self.config = config
        self.roll()

    def roll(self):
        rolls = []
        for i in range(self.config.dice):
            rolls.append(randint(1,6))
        for i in range(self.config.dice - 3):
            min_value = min(rolls)
            min_index = rolls.index(min_value)
            del rolls[min_index]
        self.value = sum(rolls)

    def skill_bonus(self):
        bonus=(-4,-3,-3,-3,-2,-2,-1,-1,-1,0,0,0,0,1,1,1,2,2,3)
        return bonus[self.value]

    def xp_bonus(self):
        bonus = (-4,-.2,-.2,-.2,-.2,-.2,-.1,-.1,-.1,0,0,0,0,.05,.05,.05,.1,.1,.1)
        return bonus[self.value]
