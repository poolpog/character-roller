from character.attribute import Attribute
from character.character_class import CharacterClass
from character.hitpoints import HitPoints
from character import cfg

class Character():
    attributes = ""
    dice = cfg.dice
    min_attribute_value = cfg.min_attribute_value

    def __init__(self, character_class = ""):
        self.attributes = {
            'str':3,
            'int':3,
            'wis':3,
            'dex':3,
            'con':3,
            'cha':3
            }

        self.character_class = CharacterClass(character_class)
        primary_attributes = self.character_class.primary_attribute_map[character_class]

        self.attributes['str']  =  Attribute(dice)
        self.attributes['int']  =  Attribute(dice)
        self.attributes['wis']  =  Attribute(dice)
        self.attributes['dex']  =  Attribute(dice)
        self.attributes['con']  =  Attribute(dice)
        self.attributes['cha']  =  Attribute(dice)

        for attribute in primary_attributes:
            while self.attributes[attribute].value < min_attribute_value:
                self.attributes[attribute] = Attribute(dice)
