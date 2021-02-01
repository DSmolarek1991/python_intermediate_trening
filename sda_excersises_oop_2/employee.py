from sda_excersises_oop_2.person import Person


class Employee(Person):
    def __init__(self, imie, nazwisko, data_urodzenia,salary):
        super().__init__(imie, nazwisko, data_urodzenia)
        self._salary=salary

    @property
    def data_urodzenia(self):
        return self._data_urodzenia

    @data_urodzenia.setter
    def data_urodzenia(self, value):
        if 1900 < self.data_urodzenia < 2021:
            self.data_urodzenia
        else:
            self.data_urodzenia = 0
    @property
    def salary(self):
        return self._salary

    def who_am_i(self):
        return f"Nazywam się {self.imie} {self.nazwisko} i zarabiam {self.salary}zł"



