from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          weapon: String, Integer
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''


        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities
        '''
        self.abilities.append(weapon)

    # def fight(self, opponent):
    #     ''' Current Hero will take turns fighting the opponent hero passed in.
    #     '''
    #
    #     hero1 = hero("Wonder Woman")
    #     hero2 = hero("Dumbledore")
    #
    #     hero1.fight(hero2)

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

    # We use the append method to add ability objects to our list.
        self.abilities.append(ability)


    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        net_damage = self.defend() - damage
        self.current_health = self.current_health - net_damage
        if damage > self.defend():
            return self.current_health - damage
        else:
            return self.current_health

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health <= 0:
            return "False"
        else:
            return "True"

    # def fight(self, opponent):
    #     ''' Current Hero will take turns fighting the opponent hero passed in.
    #     '''
    #     if ability in self.abilities <= 0:
    #         print ("Draw")
    #     else:
    #          hero1.fight(hero2)
    #          while self.current_health <= 0:


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
