class Animal:
    def __init__(self, name, age, foodPerDay,species,biome,areaPerIndividual,foodTypes=[],detachment,sound):
        self.__name = name
        self.__age = age
        self.__foodPerDay = foodPerDay
        self.__isFeeded = False
        self.__foodEated = 0
        self.__species = species
        self.__biome = biome
        self.__areaPerIndividual = areaPerIndividual
        self.__foodTypes = foodTypes
        self.__detachment = detachment
        self.__sound = sound

    @property
    def feeded(self):
        return self.__isFeeded

    def eat(self, foodType):
        if foodType not in self.__foodTypes:
            print(self.__name, 'said: Ya Takoe Ne Em Sore')
            return

        if foodType in self.__foodTypes:
            if self.__foodEated >= self.__foodPerDay:
                print(self.__name, 'said: Ya i tak Sitiy')
                self.__isFeeded = True
                return
            else:
                print(self.__name, 'ate:', foodType)
                self.__foodEated += 1
                if self.__foodEated >= self.__foodPerDay:
                    print(self.__name, 'said: Na Segodnya Vse')
                    self.__isFeeded = True

    def doSound(self, number):
        for i in range(number):
            print(self.__name, "did:", self.__sound)

    def play(self):
        print(self.__name, "did: play")