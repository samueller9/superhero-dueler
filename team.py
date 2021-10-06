class Team:

    def __init__(self, name,):
        '''
        Instance properties:
        name: String
        add_hero: String
        remove_hero: String
        view_all_heroes: list
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
    # loop through each hero in our list
        for hero in self.heroes:
        # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
            # set our indicator to True
                foundHero = True
    # if we looped through our list and did not find our hero,
    # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.
        '''
        for heroes in list:
            print(view_all_heroes)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.
        '''
        self.heroes.append(heroes)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            self.current_health = self.starting_health

     def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            if random.choice(living_heroes, living_opponents)
            return living_heroes.fight(living_opponents)
            return len.remove(living_heroes, living_opponents)
