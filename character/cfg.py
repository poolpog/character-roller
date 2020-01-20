import argparse

class Cfg():
    _2up = False
    random_class = False
    dice = 4
    allowed_classes = ( "fighter", "thief", "wizard", "cleric" )
    character_class = "fighter"
    min_primary_attr = 15

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-c", "--class",
                                help="Character class. One of: fighter, thief, wizard, cleric. Defaults to 'fighter'",
                                action="store",
                                default="fighter",
                                dest="character_class"
                                )
        parser.add_argument("-m", "--min-primary-attribute",
                                help="Minimum primary attribute value for character class. Defaults to '15'",
                                action="store",
                                type=int,
                                default=15,
                                dest="min_primary_attr"
                                )
        parser.add_argument("-2", "--2up",
                                help="Format for 2 per page, landscape",
                                action="store_true",
                                default=False,
                                dest="_2up"
                                )
        parser.add_argument("-r", "--random",
                                help="Roll a random class",
                                action="store_true",
                                default=False,
                                dest="random_class"
                                )
        parser.add_argument("-d", "--dice",
                                help="Number of dice to roll to get stats; will pick best 3",
                                action="store",
                                default=4,
                                type=int,
                                dest="dice"
                                )
        args = parser.parse_args()

        self.character_class = args.character_class
        self.min_primary_attr = args.min_primary_attr
        self._2up = args._2up
        self.random_class = args.random_class
        self.dice = args.dice if args.dice >= 3 else 3

        if args.character_class not in self.allowed_classes:
            args = parser.parse_args(['-h'])
            exit()

        if args.random_class:
            pick = randint(0, 3)
            self.character_class = self.allowed_classes[pick]

