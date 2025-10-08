import teksty as t
def pobierz():
    a=input("Podaj zdanie: ")
    b=input("Podaj szukane słowo: ")
    return a,b
a,b=pobierz()
print(f"Ilośc słów: {t.policz_slowa(a)}")
print(f"Unikalne słowa: {t.unikalne_słowa(a)}")
print(f"Czy zawiera: {t.czy_zawiera(a,b)}")