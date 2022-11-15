# Zadanie 3. Utwórz pustą listę zwierzeta. Następnie
# • Dodaj kilka nazw zwierząt do listy
# • Posortuj listę
# • Wyświetl pierwszy oraz trzy ostatnie elementy na liście
# • Wyświetl informację o liczbie zwierząt na liście

# zwierzęta = []
# y = int(input("Podaj ile dodać nazw zwierząt: "))
# for i in range(y):
#     x = input("Podaj nazwę zwierzęcia: ")
#     zwierzęta.append(x)
# #sorted
# a = zwierzęta.sorted()
# print(a)
#zad_3
zwierzeta = []
y = 0
while y < 4:
    x = input("Podaj nazwe zwierzęt: ")
    zwierzeta.append(x)
    y += 1
print(zwierzeta)
a = sorted(zwierzeta)
print(a)
print(zwierzeta[0], zwierzeta[-3:])
print(zwierzeta.sort())
print(len(zwierzeta))