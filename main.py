
# Zad1.
# Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne
def zadanie1():
    int_1 = 99
    int_2 = 123
    float_1, float_2 = 1.111, -2.222
    complex_1 = 1 + 1j
    complex_2 = 2 - 2j
    string_1 = 'łańcuch znaków 1'
    string_2 = 'łańcuch znaków 2'
    print('int: ', int_1, int_2)
    print('float: ', float_1, float_2)
    print('complex: ', complex_1, complex_2)
    print('string: ', string_1, string_2)


# zadanie1()


# Zad2.
# Stwórz skrypt kalkulator, wktórym wykorzystać wszystkie podstawowe działania arytmetyczne
def zadanie2():
    a = 20
    b = 8
    print('dodawanie:', a, '+', b, '=', a + b)
    print('odejmowanie:', a, '-', b, '=', a - b)
    print('mnożenie:', a, '*', b, '=', a * b)
    print('dzielenie:', a, '/', b, '=', a / b)
    print('dzielenie calkowite:', a, '//', b, '=', a // b)
    print('reszta z dzielenia:', a, '%', b, '=', a % b)
    print('potegowanie:', a, 'do potegi', b, '=', a ** b)
    print('potegowanie:', a, 'do potegi', b, '=', pow(a, b))


# zadanie2()


# Zad3.
# Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %
def zadanie3():
    print('a = 5')

    a = 5
    a += 7
    print('a += 7:', a)

    a = 5
    a -= 7
    print('a -= 7:', a)

    a = 5
    a *= 7
    print('a *= 7:', a)

    a = 5
    a /= 7
    print('a /= 7:', a)

    a = 5
    a **= 7
    print('a **= 7:', a)

    a = 5
    a %= 7
    print('a %= 7:', a)


# zadanie3()


# Zad4.
# Napisz skrypt, który policzy i wyświetli następujące wyrażenia:

from math import *


def zadanie4():
    print('e do potegi 10 = ', pow(e, 10))
    print('(ln(5+sin^2(8)))^(1/6) = ', pow(log(5 + pow(sin(8), 2)), 1 / 6))
    print('⌊3,55⌋ = ', floor(3.55))
    print('⌈4,80⌉ = ', ceil(4.80))


# zadanie4()


# Zad5.
# Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami.
# Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe.
# (trzeba użyć metody capitalize)
def zadanie5():
    imie = 'MATEUSZ'
    nazwisko = 'SZYMAŃSKI'
    print(str.capitalize(imie), str.capitalize(nazwisko))


# zadanie5()


# Zad6.
# Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się słowami np. „la la la”.
# Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzeba użyć metody count)
def zadanie6():
    pios = 'la la la'
    print('la powtarza sie', pios.count('la'), 'razy')


# zadanie6()


# Zad7.
# Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.
def zadanie7():
    imie = 'Mateusz'
    print('imie =', imie)
    print('imie druga litera =', imie[1])
    print('imie ostatnia litera =', imie[-1])


# zadanie7()


# Zad8.
# Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6
# i spróbuj ją podzielić na poszczególne wyrazy.(trzeba użyć metody split)
def zadanie8():
    pios = 'la la la'
    print(str.split(pios))


# zadanie8()


# Zad9.
# Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe.
# Następnie wyświetl je wykorzystując odpowiednie formatowanie.
def zadanie9():
    zm_string = 'string'
    zm_float = 123
    zm_hex = hex(255)
    print('string: {0:s}'.format(zm_string))
    print('float: {0:f}'.format(zm_float))
    print('hex: {0:s}'.format(zm_hex))


zadanie9()
