from baseAnimal import *


class baseBear(baseAnimal):
    def __init__(self, name, age):
        super().__init__(name, age, 10, 'Bear', 'Forest', 80, ['Meat'], 'Predator', 'Grrraaw')