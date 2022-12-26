#Половина кода взята у одного ученика, так как я пропустил занятие и упустил много моментов, надеюсь на понимание :) (Однако в коде я вроде разобрался)
from Zoo.importerOfTheZoo import *
class baseZoo:
    def __init__(self):
        self.valiers = []
    def addValier(self, val:Valier):
        self.valiers.append(val)
    def removeValier(self,val):
        if val not in self.valiers:
            return False
        self.valiers.remove(val)
        return True
    def addFood(self, food, number):
        for val in self.valiers:
            if food not in val.foodNeeded().keys():
                continue
            foodNeed = val.foodNeeded()[food]
            number -= foodNeed
            if number < 0:
                val.addFood(food, foodNeed - number)
            else:
                val.addFood(food, foodNeed)

    def feedAllAnimals(self):
        for val in self.valiers:
            val.feedAnimals()

    def replaseAnimal(self, fromVal: Valier, toVal: Valier, animal: baseAnimal):
        if toVal.addAnimal(animal):
            fromVal.removeAnimal(animal)

    def foodInValiers(self):
        restOfFood = {}
        for val in self.valiers:
            for foodInVal in val.foodRemaining:
                if foodInVal not in restOfFood.keys():
                    restOfFood[foodInVal] = val.foodRemaining[foodInVal]
                else:
                    restOfFood[foodInVal] += val.foodRemaining[foodInVal]
        return restOfFood