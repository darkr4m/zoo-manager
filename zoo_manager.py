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
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Reptile(Animal):
    pass

class Primate(Mammal):
    pass

class Marsupial(Mammal):
    pass

class Aviary:
    pass

class ReptileEnclosure:
    pass