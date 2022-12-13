# Zadanie 3. Napisz funkcję potęga(), która podniesie wartości z pierwszej listy do potęg z drugiej listy. Sprawdź,
# czy listy są tej samej długości. Parametrami funkcji są dwie listy. Funkcja ma zwracać listę z wynikami.

def potęga(lista_1, lista_2):
    lista_3 = []
    if len(lista_1) != len(lista_2):
        return lista_3
    for i in range(len(lista_1)):
        lista_3.append(lista_1[i]**lista_2[i])
    return lista_3

print(potęga([2,3,4], [1,2,3]))