from sda_excersises_oop_1.Cat import Cat
from sda_excersises_oop_1.Dog import Dog
from sda_excersises_oop_1.animal import Animal
from sda_excersises_oop_1.figures import Triangle, Rectangle, Circle
from sda_excersises_oop_1.vet import Vet


def main():
    class Conteiner:
        def __init__(self):
            self.cat_list = []

        def addd_cat(self, cat_name, cat_sound):
            cat1 = Cat(cat_name, cat_sound)
            self.cat_list.append(cat1)
            return self.cat_list

        def make_sound(self):
            for cat in self.cat_list:
                print(cat.make_sound())


class Painter():
    def __init__(self):
        self.lista = []

    def add_prostokat(self, hight, widght):
        prostokat = Rectangle(hight, widght).get_area()
        self.lista.append(prostokat)

    def add_kolo(self, radious):
        kolo = Circle(radious).get_area()
        self.lista.append(kolo)
    def add_trojkat(self, base,height):
        trojkat=Triangle(base,height).get_area()
        self.lista.append(trojkat)

    def all_area(self):
        return sum(self.lista)

    @staticmethod
    def farb_planer(area:float):
        if area<a.all_area():
            return True
        return False


a = Painter()
a.add_prostokat(1, 19)
a.add_kolo(100)
a.add_trojkat(12,16)
print(a.all_area())
print(a.farb_planer(32000))

if __name__ == '__main__':
    main()
