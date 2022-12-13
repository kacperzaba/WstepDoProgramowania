# Zadanie 2. Napisz funkcję sum_of_values(), która policzy i zwróci sumę wartości (values) słownika:
# dict1 = {'data1':10, 'data2':-4, 'data3':2}
# Nie wolno korzystać z funkcji sum().


def sum_of_values(dict_1):
    x = 0
    for i in dict_1.values():
        #bez i w values
        x += i
    return x


print(sum_of_values({'data1': 10, 'data2': -4, 'data3': 2}))