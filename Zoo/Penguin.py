class Penguin:

    def __init__(self, name, foodPerDay, age):
        self.Name = name
        self.Age = age
        self.FoodPerDay = foodPerDay

    def discription(self):
        self.Species = "Penguin"
        self.Biome = "Antarctica"
        self.AreaPerIndividual = 12
        self.Food = "Seafood"
        self.Detachment = "Predator"
        self.Sound = "Peckpeck"

    def eatUp(self):
        print(self.Name,"did 'Eat'")

    def doSound(self,number):
        for i in range(number):
            print(self.Name, "did", self.Sound)

    def play(self):
        print(self.Name, "did 'play'")