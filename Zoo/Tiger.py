class Tiger:

    def __init__(self, name, age, foodPerDay):
        self.__name = name
        self.__age = age
        self.__foodPerDay = foodPerDay
        self.__isFeeded = False
        self.__foodEated = 0

    def discription(self):
        self.__species = "Tiger"
        self.__biome = "Rainforests"
        self.__areaPerIndividual = 80
        self.__foodTypes = ['Meat']
        self.__predator = True
        self.__sound = "Roar"

    @property
    def Feeded(self):
        return self.__isFeeded
    def eat(self, foodType):
        if foodType not in self.__foodTypes:
            print(self.__name,'said Ya Takoe Ne Em Sore')
            return
        if self.__isFeeded:
            return
        if self.__foodEated  >= self.__foodPerDay:
            self.__isFeeded = True
            return
        if foodType in self.__foodTypes:
            print(self.__name, 'ate',foodType)
            self.__foodEated += 1
            if self.__foodEated >= self.__foodPerDay:
                self.__isFeeded = True
                self.__foodEated = 0
    def doSound(self,number):
        for i in range(number):
            print(self.__name, "did", self.__sound)
    def play(self):
        print(self.__name, "did 'play'")