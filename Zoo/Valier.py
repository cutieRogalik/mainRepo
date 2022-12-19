from Zoo.importerOfTheZoo import *


class Valier:
    def __init__(self, area, biome, detachmentOfAnimals):
        self.animals = []
        self.biome = biome
        self.area = area
        self.freeArea = area
        self.food = {}
        self.detachmentOfAnimals = detachmentOfAnimals

    def addAnimal(self, animal: baseAnimal):
        if self.biome != animal.biome or self.area < animal.areaPerIndividual or self:
            return False
        if self.detachmentOfAnimals != animal.detachment:
            return False
        else:
            if self.detachmentOfAnimals != 'Herbivore':
                return False
        if self.freeArea >= animal.areaPerIndividual:
            self.animals.append(animal)
            self.freeArea -= animal.areaPerIndividual
            return True
        else:
            return False

    def removeAnimal(self, animal):
        if animal not in self.animals:
            return False
        self.animals.remove(animal)
        self.freeArea += animal.areaPerIndividual
        return True

    def addFood(self, food, number):
        if food not in self.food.keys():
            self.food[food] = number
        else:
            self.food[food] += number

    @property
    def foodRemaining(self):
        return self.food

    def feedAnimals(self):
        for n in self.animals:
            n.eat(self.food)

    def whoIsHungry(self):
        hungryAnimals = []
        for animal in self.animals:
            if not animal.isFeeded:
                hungryAnimals.append(animal)
        return hungryAnimals

    def foodNeeded(self):
        foodNeeded = {}
        for animal in self.whoIsHungry():
            if animal.foodTypes[0] not in self.food.keys():
                foodNeeded[animal.foodTypes[0]] = animal.needFood
            else:
                foodNeeded[animal.foodTypes[0]] += animal.needFood
        return foodNeeded
