from baseAnimal import *


class baseDeer(baseAnimal):
    def __init__(self, name, age):
        super().__init__(name, age, 4, 'Ungulates', 'Forest', 70, ['Moss','Shrub','Berries'], 'Herbivore', 'Mwooaw')