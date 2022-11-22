# Zadanie 2.
# • Wypisz wszystkie pary klucz:wartość występujące w słowniku:
# sample_dict = {
#  "name": "Kelly",
#  "surname": "Jones",
#  "age": 25,
#  "salary": 8000,
#  "city": "New york"}
# • Utwórz słownik, wybierając ze słownika sample_dict pary o kluczach zapisanych w liście.
# Wskazówki:
# − przejdź za pomocą pętli po kluczach zapisanych w liście;
# − następnie sprawdź, czy dany klucz występuje w słowniku; jeśli występuje, dodaj go (parę
# klucz:wartość) do nowego słownika.
# • Usuń ze słownika wartości, których klucze występują w liście.
# • Sprawdź, czy wartość „Jones” występuje w słowniku.
# • Zmień w słowniku klucz ‘city’ na ‘location’.

sample_dict = {"name": "Kelly", "surname": "Jones", "age": 25, "salary": 8000, "city": "New york"}

print(sample_dict.keys())
print(sample_dict.values())
print(sample_dict.items())

for key, value in sample_dict.items():
    print(f"{key:<10} : {value:>10}")
# powyższe 10 - liczba pól na których zostanie wyświetlony key

list1 = ["name", "surname", "age", ]

for i in list1:
    print(i)

dnew = {}

for key in list1:
    if key in sample_dict:
        dnew[key]=sample_dict[key]
print(dnew)

for i in list1:
    sample_dict.pop(i)

print(sample_dict)

if "Js" in sample_dict.values():
    print("yes")
else:
    print("no")

sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)