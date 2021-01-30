import sound

class Cat:
    def __init__(self,name,eat = 0):
        self.name = name
        self.__eat=eat



    def make_Sound(self):
        return  f"{self.name} {sound.slownik[self.name]}"


    @property
    def eat(self):
        return self.__eat
    @eat.setter
    def eat(self,value):
        self.__eat=value

    def eat_mause(self):
        self.eat = self.eat+1


    def eat_mause_view(self):
        if self.eat ==1:
            return f"Zjadłem {self.eat} mysz!!"
        return f"Zjadłem {self.eat} myszy!!"





cat1 = Cat('cat1')
cat1.eat_mause()
print(cat1.eat_mause_view())




