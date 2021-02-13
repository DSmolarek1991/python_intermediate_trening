'''
3. Napisz klasę Complex do obsługi liczb zespolonych. Klasa powinna posiadać:
a) Konstruktor – z jednym parametrem
b) Następnie dodaj drugi parametr z wartością domyślną, czyli gdy część urojona jest
równa zero
c) Metodę show wypisującą liczbę w postaci a + b*i (pamiętaj o przypadkach, gdy
część urojona jest równa zero lub mniejsza od zera)
4. Zamiast metody show nadpisz metodę __str__.
5. Do klasy Complex dopisz metodę is_equal_to, która sprawdzi, czy bieżący obiekt ma
takie same części rzeczywistą i urojoną jak liczba przekazana w parametrze tej funkcji.
Przykład:
z1 = 3 + 5i
z2 = 3 + 5i
z3 = 5 + 3i
z1. is_equal_to(z2) // true
z2. is_equal_to(z3) // false
6. Zamiast metody is_equal_to nadpisz metodę __eq__.
'''

class Complex:
    def __init__(self,real,complex = 0):
        self._real = real
        if complex <=0 :
            self._complex = 0
        else:
            self._complex = complex

    def show(self):
        if self._complex <= 0: return f"{self._real}"
        return f"{self._real} + {self._complex}*i"

    def __str__(self):
        if self._complex <= 0: return f"{self._real}"
        return f"{self._real} + {self._complex}*i"

    def is_equal_to(self,other):
        return  self._real== other._real and self._complex == other._complex

    def __eq__(self, other):
        return self._real ==  other._real and self._complex == other._complex


    @staticmethod
    def add(z1,z2):
        return f"{z1._real+z2._real} + {z1._complex+z2._complex}*i"


    #@staticmethod
    def add_v2(self, other):
        real = self._real + other._real
        im = self._complex + other._complex
        return Complex(real,im)













z1 = Complex(3,5)
z2 = Complex(3,5)
z3=Complex(5,3)

print(z1.is_equal_to(z2))
print(z2.is_equal_to(z3))
print(z1.__eq__(z2))
print(z2.__eq__(z3))
print(Complex.add(z1,z2))
print(z1.add_v2(z2))
print(sum(z1,z3))
