class Elephant:

    def __init__(self, name, foodPerDay, age):
        self.Name = name
        self.Age = age
        self.FoodPerDay = foodPerDay

    def discription(self):
        self.Species = "Elephant"
        self.Biome = "Desert"
        self.AreaPerIndividual = 500
        self.Food = "Grass and Hay"
        self.Detachment = "Herbivore"
        self.Sound = "Woom"

    def eatUp(self):
        print(self.Name,"did 'Eat'")

    def doSound(self,number):
        for i in range(number):
            print(self.Name, "did", self.Sound)

    def play(self):
        print(self.Name, "did 'play'")
