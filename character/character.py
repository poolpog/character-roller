from character.attribute import Attribute, Attribute5e, AttributeBasic
from character.character_class import CharacterClass
from character.hitpoints import HitPoints

from character.cfg import Cfg

class Character():
    attributes = ""

    def __init__(self, config):
        self.attributes = {
            'str':3,
            'int':3,
            'wis':3,
            'dex':3,
            'con':3,
            'cha':3
            }

        self.config = config
        self.character_class = CharacterClass(config)
        self.hit_points = HitPoints(config)
        self.bonus_modified = {}
        primary_attributes = self.character_class.primary_attribute_map[config.character_class]

        if self.config.edition == "5e":
            self.attributes['str']  =  Attribute5e(config)
            self.attributes['int']  =  Attribute5e(config)
            self.attributes['wis']  =  Attribute5e(config)
            self.attributes['dex']  =  Attribute5e(config)
            self.attributes['con']  =  Attribute5e(config)
            self.attributes['cha']  =  Attribute5e(config)
        else:
            self.attributes['str']  =  AttributeBasic(config)
            self.attributes['int']  =  AttributeBasic(config)
            self.attributes['wis']  =  AttributeBasic(config)
            self.attributes['dex']  =  AttributeBasic(config)
            self.attributes['con']  =  AttributeBasic(config)
            self.attributes['cha']  =  AttributeBasic(config)
        
        self.bonus_modified['hp'] = self.hit_points.value + ( self.config.level * self.attributes['con'].skill_bonus() )

        for attribute in primary_attributes:
            while self.attributes[attribute].value < config.min_primary_attr:
                self.attributes[attribute].roll()
