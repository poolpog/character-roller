from character.cfg import Cfg

class CharacterClass():
    name = ""
    primary_attribute_map = {
        'fighter':   ['str'],
        'wizard':    ['int'],
        'cleric':    ['wis'],
        'thief':     ['dex'],
        'dwarf':     ['str','con'],
        'elf':       ['str','int'],
        'halfling':  ['str','dex']
    }

    def __init__(self,config):
        self.config = config
        self.name = config.character_class

    def get_primary_attributes():
        return primary_attribute_map[name]

    def get_name():
        return name
