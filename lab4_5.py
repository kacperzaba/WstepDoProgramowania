# Zadanie 5. Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
# Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
# • Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
# • Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
# punktów nie występuje na liście, wyświetl odpowiedni komunikat
# • Oblicz średnią punktów liczbę punktów z egzaminu
# • Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
# • Wyświetl punkty poniżej średniej
# • Wyświetl punkty powyżej średniej

import random

punkty = []
for i in range(15):
    points = random.uniform(0, 50)
    points2 = round(points, 2)
    punkty.append(points2)
print(punkty)
max_punkty = max(punkty)
print(f"Największ ilość punktów: {max_punkty}")
min_punkty = min(punkty)
print(f"Najmniejsza ilość punktów: {min_punkty}")

x = float(input("Wybrana wartość: "))
if x in punkty:
    print(f"Indeks podanej wartośći: {punkty.index(x)}")
else:
    print("Podana wartość nie znajduje się na liście.")
y = round(sum(punkty)/len(punkty), 2)
print(f"Średnia punktów z egzaminu wynosi: {y}")

lista1 = []
for i in punkty:
    if i < y:
        lista1.append(i)
print(len(lista1))
print(lista1)

lista2 = [i for i in punkty if i > y]
print(len(lista2))
print(lista2)