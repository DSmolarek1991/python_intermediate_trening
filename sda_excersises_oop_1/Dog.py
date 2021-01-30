import sound

class Dog:
    def __init__(self,name):
        self.name = name

    def make_sound(self):
        return f"{self.name} {sound.slownik[self.name]}"




