class Person:
    def __init__(self, imie, nazwisko, data_urodzenia):
        self._imie = imie
        self._nazwisko = nazwisko
        self._data_urodzenia = data_urodzenia

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self, value):
        self._imie = value

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, value):
        self._nazwisko = value

    @property
    def data_urodzenia(self):
        return self._data_urodzenia

    @data_urodzenia.setter
    def data_urodzenia(self, value):
        self._data_urodzenia = value



