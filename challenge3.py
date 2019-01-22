# Sprytne potęgowanie. Napisz funkcję, która oblicza zadaną potęgę w podany sposób: wywołuje rekurencyjnie samą siebie dla wykładnika podzielonego na dwa, a następnie operując na tym częściowym wyniku oblicza pełną potęgę.

"""
def cleverPower(base, index):

    if index == 0:
        return 1

    if index == 1:
        return base

    halfIndex = cleverPower(base, index // 2)
    if index % 2 == 0:
        return halfIndex * halfIndex
    else:
        return halfIndex * halfIndex * base


def main():

    base = int(input())
    index = int(input())
    print(cleverPower(base, index))


if __name__ == "__main__":

    main()
"""

# Palindromy. Napisz funkcję czyPalindrom(), która zwraca prawdę, gdy podany jako argument napis jest palindromem, to znaczy czytany wspak da ten sam napis, np. “kajak”. Funkcja zwraca fałsz w przeciwnym wypadku.

"""
def isPalindrom(sample_text):

    for i in range(len(sample_text) // 2):
        if sample_text[i] == sample_text[-1 - i]:
            return True
        else:
            return False


def main():

    print("Podaj napis do sprawdzenia: ")
    sample_text = input()
    print(isPalindrom(sample_text))


if __name__ == "__main__":

    main()
    
"""

# Anagram. Napisz funkcję czyAnagram(), która zwraca prawdę, gdy dwa napisy podane jako dwa argumenty funkcji mają tę własność, że da się z liter pierwszego napisu ułożyć drugi napis.

# def czyAnagram(napis1, napis2):
    # if len(napis1) != len(napis2):
    #     return False
    #
    # slownik1 = dict()
    # slownik2 = dict()
    #
    # for i in range(len(napis1)):
    #
    #     if napis1[i] in slownik1:
    #         slownik1[napis1] += 10+
    #     else:
    #         slownik1[napis1] = 1
    #     if napis2[i] in slownik2:
    #         slownik2[napis2] += 1
    #     else:
    #         slownik2[napis2] = 1
    # return slownik1 == slownik2

"""
def isAnagram(text1, text2):

    for char in text2.lower():
        if char not in text1.lower():
            return False
    else:
        return True


def main():

    while True:
        text1 = input("Pierwszy napis do sprawdzenia: ")
        text2 = input("Drugi napis do sprawdzenia: ")
        if isAnagram(text1, text2):
            print("\n{0} jest anagramem {1}.".format(text2, text1))
        else:
            print("\n{0} NIE jest anagramem {1}.".format(text2, text1))

        answer = input("\nCzy chcesz powtórzyć test? [t/n] ")
        if answer != 't':
            break


if __name__ == "__main__":
    
    main()

"""


# Moda. Napisz funkcję moda(), która jako parametr przyjmuje listę liczb całkowitych. Funkcja zwraca tę liczbę, która pojawia się w tej liście najczęściej. Jeśli mamy remis, zwróć którąkolwiek z tych liczb.




def moda(int_list):

    int_list = list(int_list)
    for i in int_list:
        int_list.count(i)

def main():

    print("Podaj liczby:\n")
    int_list = input()
    moda(int_list)


if __name__ == "__main__":
    main()





