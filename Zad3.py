def pobierz():
    zmien = input ("Podaj listę wyników: ")
    if(not bool(zmien)):
        raise ValueError
    zmien = zmien.split()
    return zmien

os1 = pobierz()
os2 = pobierz()
os1 = set(os1)
os2 = set(os2)


print(f"Uniq: {os1 ^ os2}, {'\n'}Wspolne: {os1 & os2}, {'\n'}Łącznie: {os1 | os2}") # type: ignore