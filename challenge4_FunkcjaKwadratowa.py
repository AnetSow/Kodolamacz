"""Napisz klasę FunkcjaKwadratowa, która przechowuje funkcje typu 𝑎𝑥2+bx+c. Klasa powinna zawierać trzy pola: a, b, c, które są przypisywane w konstruktorze. Główną metodą powinna być Rozwiaz(), która zwraca miejsca zerowe podanej funkcji. Należy zwrócić uwagę na przypadki gdy a=0, b=0 lub c=0, a także obmyślić sposób informowania o nieskończonej liczbie, jednym lub zerze rozwiązań."""


import math

class FunkcjaKwadratowa:

    def __init__(self, a, b, c):   # konstruktor
        self.a = a
        self.b = b
        self.c = c


    def rozwiaz(self):
        print("Rozwiąż równanie {0}*x^2 + {1}*x + {2}".format(self.a, self.b, self.c))

        if self.a == 0 and self.b == 0:
            if self.c == 0:
                return float("inf"), float("inf")
            else:
                return float("nan"), float("nan")
        if self.a == 0:
            return -self.c/self.b, -self.c/self.b

        delta = self.b ** 2 - 4 * self.a * self.c

        if delta > 0:
            x1 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b + math.sqrt(delta)) / (2 * self.a)

            return x1, x2

        elif delta == 0:
            x0 = -self.b / (2 * self.a)

            return x0

        if delta < 0:
            return float("nan"), float("nan")


def main():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    f = FunkcjaKwadratowa(a, b, c)

    print("Rozwiązanie to: {}".format(f.rozwiaz()))

if __name__ == "__main__":
    main()