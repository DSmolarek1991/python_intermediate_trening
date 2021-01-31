from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def get_area(self):
        return 0.0


