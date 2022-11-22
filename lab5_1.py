# Zadanie 1.
# • Utwórz listę values zawierającą liczby 10, 20, 30. Utwórz drugą listę keys zawierającą nazwy tych liczb w
# języku angielskim (lub polskim). Dokonaj konwersji tych list w słownik.
# Wskazówki:
# − użyj funkcji zip(), która pobiera dwie sekwencje (takie jak list, dict, str), łączy je w krotki (pary) i
# zwraca;
# − lub wykonaj iterację listy za pomocą pętli for i funkcji range(). W każdej iteracji dodaj nową parę kluczwartość do słownika.
# • Utwórz drugi słownik metodą słów kluczowych ( dict(klucz1=wartość1, klucz2=wartość2)), gdzie kluczem
# będą nazwy liczb 30, 40, 50, a wartościami – liczby 30, 40, 50.
# • Połącz dwa słowniki w jeden nowy słownik.

values = [10, 20, 30]
keys = ["ten", "twenty", "thirty"]

d1 = {}
for i in range(len(keys)):
    d1[keys[i]] = values[i]
print(d1)

#słownik składany:
d1 = {keys[i]:values[i] for i in range(len(keys))}
print(d1)

d1 = dict(zip(keys, values))
print(d1)

d2 = dict(thirty=30, fourty=40, fifty=50)
print(d2)

dnew = d1
dnew.update(d2)
print(dnew)

