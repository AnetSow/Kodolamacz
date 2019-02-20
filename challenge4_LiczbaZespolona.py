"""Napisz klasę Zespolona, która przechowuje liczby zespolone: a+bi. Niech część rzeczywista nazywa się re, a urojona im. Zdefiniuj metody: modul(), oblicza moduł liczby zespolonej oraz dodaj() i mnoz() (statyczne) – obliczają odpowiednio sumę i iloczyn dwóch liczb zespolonych."""

import math


class Zespolona:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def modul(self):
        return math.sqrt(self.re ** 2 + self.im ** 2)

    @staticmethod
    def dodaj(z1, z2):
        return Zespolona(z1.re + z2.re, z1.im + z2.im)

    @staticmethod
    def mnoz(z1, z2):
        return Zespolona(z1.re * z2.re - z1.im * z2.im, z1.im * z2.re + z1.re * z2.im)

    def __str__(self):
        return "re = %s, im = %s" % (self.re, self.im)

def main():
    print("Podaj część rzeczywista i część urojoną pierwszej liczby zespolonej: ")
    re = int(input("re = "))
    im = int(input("im = "))
    z1 = Zespolona(re=re, im=im)

    print("Podaj część rzeczywista i część urojoną drugiej liczby zespolonej: ")
    re2 = int(input("re = "))
    im2 = int(input("im = "))
    z2 = Zespolona(re=re2, im=im2)

    print("\nModul 1-szej liczby: {0} \nModul 2-giej liczby: {1} \nSuma liczb: {2} \nIloczyn liczb: {3}".format(z1.modul(), z2.modul(), Zespolona.dodaj(z1, z2), Zespolona.mnoz(z1, z2)))


if __name__ == "__main__":
        main()
