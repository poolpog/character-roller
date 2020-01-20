from character import cfg

class Attribute():
    value = 0
    bonus_strings = {
        'str': '{:>+2d} melee,{:>+2d} dmg,{:>+3.0f}% xp',
        'int': '{:>+2d} languages,{:>+3.0f}% xp',
        'wis': '{:>+2d} save v spell,{:>+3.0f}% xp',
        'dex': '{:>+2d} missle,{:>+2d} AC,{:>+3.0f}% xp',
        'con': '{:>+2d} HP',
        'cha': '{:>+2d} NPC react'
    }
    dice = cfg.dice

    def __init__(self):
        self.roll()

    def roll(self):
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
