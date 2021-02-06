from sda_excersises_oop_1.figure import Figure
from math import pi


class Rectangle(Figure):
    def __init__(self, high: float, width: float):
        self.hight = high
        self.width = width

    def get_area(self)->float:
        return self.hight * self.width


class Circle(Figure):
    def __init__(self, radious: float):
        self.radious = radious

    def get_area(self)->float:
        return pi * self.radious ** 2.0


class Triangle(Figure):
    def __init__(self, high: float, base: float):
        self.high = high
        self.base = base

    def get_area(self)->float:
        return self.high * self.base / 2.0
