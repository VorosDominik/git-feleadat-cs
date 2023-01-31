# megoldas

def pontszamitas(lapok):
    ertek = 0
    for i in range(len(lapok)):
        ertek += lapok[i]
    return ertek


def eredemeny(geplapok, jlapok):
    gep = pontszamitas(geplapok)

    j = pontszamitas(jlapok)

    if gep > 21 and j > 21:
        return "senki sem nyert"
    elif gep > 21:
        return "gep vesztett"
    elif j > 21:
        return "j vesztett"


# teszt esetek
def kiiras(szoveg):
    print(szoveg)
