from ability import Ability
import random
from random import randint


class Weapon(Ability):

    def __init__(self, name, max_damage):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_value = random.randint(50,self.max_damage)
        return random_value
