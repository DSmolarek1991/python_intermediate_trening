'''
1. Dla podanej liczby oznaczającej numer dnia tygodnia, wypisz nazwę tego dnia. Użyj
kolekcji dict.
'''


class Week:
    kalendarz = {
        1:'poniedziałek',
        2: 'wtorek',
        3: 'środa',
        4: 'czwartek',
        5: 'piątek',
        6: 'sobota',
        7: 'niedziela' }
    def get_day(self,value):
        return self.kalendarz.get(value)


week = Week()
print(week.get_day(4))

