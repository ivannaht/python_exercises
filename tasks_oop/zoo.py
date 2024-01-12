class Animal():
    """
    class Animal that stores the animal's name, species, and number of legs.
    """

    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def make_sound(self):
        raise ValueError("Should be overriden in the subclasses")


class Mammal(Animal):
    """
    class Mammal inherit the name, species, and number of legs from the Animal class.
    """

    def __init__(self, name, species, legs):
        super().__init__(name, species, legs)

    def give_birth(self):
        return True

    def make_sound(self):
        return "Roar"


class Bird(Animal):
    """
    class Bird inherit the name, species, and number of legs from the Animal class.
    """

    def __init__(self, name, species, legs):
        super().__init__(name, species, legs)

    def lay_eggs(self):
        return True

    def make_sound(self):
        return "Squawk"


class Reptile(Animal):
    """
    class Reptile inherit the name, species, and number of legs from the Animal class.
    """

    def __init__(self, name, species, legs):
        super().__init__(name, species, legs)

    def shed_skin(self):
        return True

    def make_sound(self):
        return "Hiss"


animals = [Mammal("Lion", "Mammal", 4), Bird("Falcon", "Bird", 2), Reptile("Python", "Reptile", 4)]
print(animals[0].make_sound())
print(animals[1].lay_eggs())

for animal in animals:
    print(f"Animal: {animal.name}, Species: {animal.species}, Legs: {animal.legs}, Sound: {animal.make_sound()}")