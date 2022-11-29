# Zadanie 3. Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
# Następnie zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną.
# Wskazówka: użyj parametru *args, który łączy wszystkie dodatkowe (nadmiarowe) argumenty
# pozycyjne, niebędące słowami kluczowymi podczas wywoływania funkcji, w krotkę.


# def zad3(*args):
#     for i in args:
#         print(i)
#
#
# zad3(3, 3.2, "kot", ["mysz", 55])
# zad3(4.44444444, "adfgdaf")

def max(*args):
    a = args[0]
    for i in args[1:]:
       if a < i:
          a = i
    return a

print(max(5, 44, 4, 12, 4))