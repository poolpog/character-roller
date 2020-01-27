from character.cfg import Cfg

class CharacterClass():
    name = ""
    primary_attributes = {
        'fighter':   ['str','con'],
        'wizard':    ['int','wis'],
        'cleric':    ['wis','cha'],
        'thief':     ['dex','int'],
    }

    def __init__(self,config):
        self.config = config
        self.name = config.character_class

    def get_primary_attributes():
        return primary_attributes[name]

    def get_name():
        return name

class CharacterClass5e():
    name = ""
    primary_attributes = {
        'barbarian':['str','con'],
        'bard':     ['dex','cha'],
        'cleric':   ['wis','cha'],
        'druid':    ['wis','int'],
        'fighter':  ['str','con'],
        'monk':     ['str','dex'],
        'paladin':  ['wis','cha'],
        'ranger':   ['str','dex'],
        'rogue':    ['dex','int'],
        'sorcerer': ['con','cha'],
        'warlock':  ['wis','cha'],
        'wizard':   ['int','wis'],
    }

    def __init__(self,config):
        self.config = config
        self.name = config.character_class

    def get_primary_attributes():
        return primary_attributes[name]

    def get_name():
        return name

class CharacterClassBasic():
    name = ""
    primary_attributes = {
        'fighter':   ['str'],
        'magicuser': ['int'],
        'cleric':    ['wis'],
        'thief':     ['dex'],
        'dwarf':     ['str'],
        'elf':       ['str'],
        'halfling':  ['str']
    }

    def __init__(self,config):
        self.config = config
        self.name = config.character_class

    def get_primary_attributes():
        return primary_attributes[name]

    def get_name():
        return name
