def policz_slowa(tekst:str):
    return len(tekst.split())
def unikalne_słowa(tekst:str):
    return set(tekst.split())
def czy_zawiera(tekst:str, słowo:str):
    return słowo in tekst