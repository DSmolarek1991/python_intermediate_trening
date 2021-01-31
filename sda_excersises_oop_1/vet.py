from sda_excersises_oop_1 import Cat, Dog
from sda_excersises_oop_1.animal import Animal


class Vet:
    @staticmethod
    def say_cat_hello(cat:Cat):
        print(f"Witaj {cat.name}")
    @staticmethod
    def say_dog_hallo(dog:Dog):
        print(f"Witaj {dog.name}")
    @staticmethod
    def say_animal_hello(animal:Animal):
        print(f"Witaj {animal.name}")




