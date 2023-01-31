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
    def teszt_esetek():
        jatekos_vesztett_teszt()

    def jatekos_vesztett_teszt():
        jatekos = [10, 9, 3]
        gep = [10, 9]
        vart_eredmeny = "j vesztett"
        kapott_eredmeny = eredemeny(gep, jatekos)
        if kapott_eredmeny == vart_eredmeny:
            print("teszt sikeres")
        else:
            print("nem sikerult")

    teszt_esetek()

