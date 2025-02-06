"""
Zoo animal Manager
Classes:
    - Animal (parent class)
        - Mammal
            - Primate
            - Marsupial
        - Bird
        - Reptile
    Aviary
    ReptileEnclosure

    Animal - class
        name - string - Represents the name of the animal
        species - string - Repesents the species of the animal (scientific name)
        #speak
            returns string representing sound the animal makes
    Mammal - class (animal)
        #give_birth
            prints message indicating that the mammal has given birth
    Primate - class (mammal)
        #climb_trees
            prints message that the primate is climbing trees
    Marsupial - class (mammal)
        #carry_baby
            prints message that the marsupial is carrying its baby
    Bird - class (animal)
        wingspan - int - represents the wingspan of the bird in meters
    Reptile - class (animal)
        #bask_in_sun
            prints a message indicating that the reptile is basking in the sun
    Aviary - class
        birds - [Bird] - list of bird instances
    ReptileEnclosure - class
        repriles - [Reptile] - list of reptile instances
"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return 'Animal sound'

class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"

class Bird(Animal):
    def __init__(self,name,species,wingspan):
        super().__init__(name,species)
        self.wingspan = wingspan

class Reptile(Animal):
    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"

class Primate(Mammal):
    def climb_trees(self):
        return f"{self.name} the {self.species} is climbing trees"

class Marsupial(Mammal):
    def carry_baby(self):
        return f"{self.name} the {self.species} is carrying its baby"

class Aviary:
    def __init__(self):
        self.birds = []

class ReptileEnclosure:
    def __init__(self):
        self.reptiles = []