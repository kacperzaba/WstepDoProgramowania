# Napisz pętlę nieskończoną, w której użytkownik podaje liczby całkowite. W przypadku liczby
# ujemnej, następuję wyjście z pętli.

while True:
    number = int(input("Podaj liczbę: "))
    if number < 0:
        break
        