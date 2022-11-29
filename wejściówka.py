#Grupa 1. Użytkownik podaje 5 liczb. Zapisz do listy tylko liczby nieparzyste większe od 10.
lista = []
for i in range(5):
    podana_liczba = int(input("Podaj liczbę: "))
    if podana_liczba > 10 and podana_liczba % 2:
        lista.append(podana_liczba)

print(lista)