# Zmodyfikuj program z zad. 1 tak, aby przechodząc po kolejnych liczbach przedziału, wypisywać
# tylko liczby parzyste, a nieparzyste – pomijać. Użyj instrukcji continue.

a=int(input("Proszę podać a "))
b=int(input("Proszę podać b "))
if a > b:
    a, b = b, a
while a <= b:
    a += 1
    if a % 2:
        pass
    print(a, end=" ")

a=int(input("Proszę podać a "))
b=int(input("Proszę podać b "))
if(a>b):
    c=b
    d=a
else:
    c=a
    d=b
while(c<=d):
    if c%2:
        c+=1
        continue
    print(c, end=" ")
    c+=1