from sda_excersises_oop_1.Cat import Cat
from sda_excersises_oop_1.Dog import Dog


def main():
    lista = [Cat('cat1'),Dog('dog1')]
    for animal in lista:
        print(animal.make_sound())


if __name__ == '__main__':
    main()