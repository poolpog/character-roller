from character.attribute import Attribute
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

        self.attributes['str']  =  Attribute(config)
        self.attributes['int']  =  Attribute(config)
        self.attributes['wis']  =  Attribute(config)
        self.attributes['dex']  =  Attribute(config)
        self.attributes['con']  =  Attribute(config)
        self.attributes['cha']  =  Attribute(config)
        
        self.bonus_modified['hp'] = self.hit_points.value + ( self.config.level * self.attributes['con'].skill_bonus() )

        for attribute in primary_attributes:
            while self.attributes[attribute].value < config.min_primary_attr:
                self.attributes[attribute] = Attribute(config)
