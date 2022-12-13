# Zadanie 4.Napisz funkcję znaki(), która zlicza znaki w string’u za pomocą słownika: znaki stanowią klucze, liczba
# znaków – wartości. Parametrem funkcji jest string. Funkcja ma zwracać słownik z wynikami. Wypisz słownik
# uporządkowany według kluczy.
# Wskazówka: użyj metody get(), która przy dostępie do wartości klucza, którego nie ma w słowniku,
# zgłasza wyjątek KeyError. Aby uniknąć tego błędu metoda get może zwrócić wartość zdefiniowaną przez
# użytkownika (drugi parametr).
# Np. Wejście: „znaki napisu”
# Wyjście: {'z': 1, 'n': 2, 'a': 2, 'k': 1, 'i': 2, ' ': 1, 'p': 1, 's': 1, 'u': 1}

def znaki(napis):
    dict_1 = {}
    for i in napis:
        dict_1[i] = dict_1.get(i, 0) + 1
        # if i in dict_1:
        #     dict_1[i] += 1
        #
        # else:
        #     dict_1[i] = 1

    return dict_1

dict_2 = znaki("samochódao")

for i in sorted(dict_2.keys()):
    print(i, dict_2[i])




