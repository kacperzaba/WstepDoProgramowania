# Zadanie 5. Napisz program działający jak prosty kalkulator. W tym celu utwórz funkcje dodawanie(),
# odejmowanie(), mnożenie() oraz dzielenie(). Następnie utwórz słownik, którego kluczem jest działanie, a
# wartością – nazwa odpowiedniej funkcji.
# Uwaga: funkcja jest obiektem, a nazwa funkcji – nazwą (referencją) tego obiektu.

kalkulator = {}

def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnożenie(a, b):
    return a * b
def dzielenie(a, b):
    if b != 0:
        return a / b

kalkulator = {"+": dodawanie, "-": odejmowanie, "*": mnożenie, "/":dzielenie}

u1 = float(input("Podaj liczbę: "))
u2 = float(input("Podaj liczbę: "))
działanie = input("Podaj działanie: ")

print(kalkulator[działanie](u1, u2))