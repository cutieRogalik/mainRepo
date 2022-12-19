from baseAnimal import *


class baseWolf(baseAnimal):
    def __init__(self, name, age):
        super().__init__(name, age, 5, 'Wolf', 'Forest', 50, ['Meat'], 'Predator', 'Hgrrr')
