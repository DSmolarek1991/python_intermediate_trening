from sda_excersises_oop_1 import sound
from sda_excersises_oop_1.Movable import Movable


class Cat(Movable):
    def __init__(self, name, eat=0):
        self.name = name
        self.__eat = eat

    def make_sound(self):
        return f"{self.name} {sound.slownik[self.name]}"

    @property
    def eat(self):
        return self.__eat

    @eat.setter
    def eat(self, value):
        self.__eat = value

    def eat_mause(self):
        self.eat = self.eat + 1

    def eat_mause_view(self):
        if self.eat == 1:
            return f"Zjadłem {self.eat} mysz!!"
        return f"Zjadłem {self.eat} myszy!!"

    def move(self):
        print('idę')
