
class Pet:

    def __init__(self, name,):
        '''Instance properties:
        name: String
        '''
        self.name = name


    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Pet):
    def __init__(self,name):
        super().__init__(name)

    def sound(self):
        return 'bark'

class Cat(Pet):
    def __init__(self,name):
        super().__init__(name)

    def sound(self):
        return 'meow'

class Fish(Pet):
    def __init__(self,name):
        super().__init__(name)

    def sound(self):
        return 'blurp'

pets = [Dog('Pet1'), Cat('Pet2'), Fish('Pet3')]

for pet in pets:
    print(pet.name + ", " + pet.sound())
