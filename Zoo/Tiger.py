class Tiger:

    def __init__(self, name, foodPerDay, age):
        self.Name = name
        self.Age = age
        self.FoodPerDay = foodPerDay

    def discription(self):
        self.Species = "Tiger"
        self.Biome = "Rainforests"
        self.AreaPerIndividual = 80
        self.Food = "Meat"
        self.Detachment = "Predator"
        self.Sound = "Roar"

    def eatUp(self):
        print(self.Name,"did 'Eat'")

    def doSound(self,number):
        for i in range(number):
            print(self.Name, "did", self.Sound)

    def play(self):
        print(self.Name, "did 'play'")