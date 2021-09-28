
import hero
import random

def fight(self, opponent):
    ''' Current Hero will take turns fighting the opponent hero passed in.
    '''

    hero1 = hero("Wonder Woman")
    hero2 = hero("Dumbledore")

    hero1.fight(hero2)

    print(random.choice(hero))
