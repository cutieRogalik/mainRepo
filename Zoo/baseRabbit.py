from baseAnimal import *


class baseRabbit(baseAnimal):
    def __init__(self, name, age):
        super().__init__(name, age, 6, 'Small Mammals', 'Forest', 2.5, ['Herb','Hay','Berries'], 'Herbivore', 'Sniff-Sniff')