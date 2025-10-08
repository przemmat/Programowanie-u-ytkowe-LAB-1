from typeguard import typechecked

def pobierz() -> list[float]:
    """
    Funkcja pobiera z terminala ciąg liczb oddzielonych spacją, dzieli je na tablicję stringów i converteruje ją na tablicę float którą następnie zwraca
    tyle.
    """

    zmien = input ("Podaj listę wyników: ")
    if(not bool(zmien)):
        raise ValueError
    zmien = zmien.split()
    wynik = [float(i) for i in zmien]
    return wynik
@typechecked
def operacje(x:list [float])->tuple[float,float,float]:
    if(not bool(x)):
        raise ValueError
    """
    suma =0 
    ile =0
    test =lambda a: a>0
    for item in x:
        if test(item):
            suma+=item
            ile+=1"""
    posList=[item for item in x if item >0]
    suma=sum(posList)
    ile=len(posList)

    return (suma,ile,suma/ile)



zmien = pobierz()
wynik=operacje(zmien)
suma,ilosc,srednia = wynik
print(f"Suma: {suma} Ilośc: {ilosc} Srednia: {srednia}")
 