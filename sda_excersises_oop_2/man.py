from sda_excersises_oop_2.employee import Employee


class Manager(Employee):
    def __init__(self, imie, nazwisko, data_urodzenia, salary:float):
        super().__init__(imie, nazwisko, data_urodzenia, salary)

    @property
    def get_salary(self)->float:
        return self.salary

    @get_salary.setter
    def get_salary(self):
        self.salary=self.salary*10

    def who_am_i(self):
        return f"Nazywam się manager {self.imie} {self.nazwisko} i zarabiam {self.get_salary}"
