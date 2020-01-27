from character.cfg import Cfg

class Race():
    name = ""
    primary_attributes = {
        'elf':      ['str','con'],
        'dwarf':    ['int','wis'],
        'human':    ['wis','cha'],
        'halfling': ['dex','int'],
    }

    def __init__(self,config):
        self.config = config
        self.name = config.race

    def get_primary_attributes():
        return primary_attributes[name]

    def get_name():
        return name

class Race5e():
    name = ""
    primary_attributes = {
    }

    def __init__(self,config):
        self.config = config
        self.name = config.race

    def get_primary_attributes():
        return primary_attributes[name]

    def get_name():
        return name

class RaceBasic():
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
        self.name = config.race

    def get_primary_attributes():
        return primary_attributes[name]

    def get_name():
        return name
