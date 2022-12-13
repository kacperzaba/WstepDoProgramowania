#wypisać to nie znaczy zwrócić!

#
# Zadanie 1. Napisz funkcję find(), która w liście sprawdza czy występuje podana wartość. Lista i wartość są
# parametrami funkcji. Funkcja ma zwracać listę indeksów, pod którymi wystąpiła wartość. Nie wolno korzystać z
# operatora in w celu sprawdzenia czy wartość występuje w liście.



def find(lista, wartość):
    lista_2 = []
    for i in range(len(lista)):
        if lista[i] == wartość:
            lista_2.append(i)
    return lista_2

print(find([2, 3, 44, 33, 2, 23, 23], 2))

print(find("samochód", "a"))


