def main():
    while True:
        print("Podaj liczbę, operację +,-,*,/,%, a następnie kolejną liczbę:")
        num1 = int(input())
        sign = input()
        num2 = int(input())

        if sign == '+':
            wynik = num1 + num2
        elif sign == '-':
            wynik = num1 - num2
        elif sign == '*':
            wynik = num1 * num2
        elif sign == '/':
            wynik = num1 / num2
        elif sign == '%':
            wynik = num1 % num2
        else:
            print("Niepoprawna operacja")
            break

        print("Twój wynik to: " + str(wynik))

        print("Chcesz wykonać kolejne działanie? Wpisz literę t lub n.")

        next_operation = input()
        if next_operation == 't':
            continue
        elif next_operation == 'n':
            break


if __name__ == "__main__":
    main()
