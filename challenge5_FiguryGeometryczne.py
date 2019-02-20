"""Stwórz hierarchię klas reprezentujących figury geometryczne. Każda figura powinna umieć wypisać informacje o sobie, a także obliczyć swój obwód i pole."""

from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def typ(self):
        pass

    @abstractmethod
    def obwod(self):
        pass

    @abstractmethod
    def pole(self):
        pass

    def wynik(self):
        print("\n{0} o obwodzie {1} cm i polu {2} cm2.".format(self.typ(), self.obwod(), self.pole()))

class Kolo(Figura):
    def __init__(self, r):
        self.r = r

    def typ(self):
        return "Koło"

    def obwod(self):
        return 2 * math.pi * self.r

    def pole(self):
        return math.pi * self.r ** 2

class Prostokat(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def typ(self):
        return "Prostokąt"

    def obwod(self):
        return 2 * self.a + 2 * self.b

    def pole(self):
        return self.a * self.b

class Kwadrat(Figura):
    def __init__(self, a):
        self.a = a

    def typ(self):
        return "Kwadrat"

    def obwod(self):
        return 4 * self.a

    def pole(self):
        return self.a ** 2


def main():
    x = int(input("\nPodaj długość boku kwadratu: \n"))
    a = Kwadrat(x)
    a.wynik()

    y = int(input("\nPodaj długość promienia koła: \n"))
    b = Kolo(y)
    b.wynik()


    p = Prostokat(2, 3)
    p.wynik()


if __name__ == "__main__":
    main()