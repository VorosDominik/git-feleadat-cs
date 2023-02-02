# megoldas

def pontszamitas(lapok):
    ertek = 0
    for i in range(len(lapok)):
        ertek += lapok[i]
    return ertek


def eredemeny(jlapok , geplapok ):
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
    jatekos_vesztett()
    r_gep21()
    r_gep21_21kevesebblap()
    r_tultoltes()

def jatekos_vesztett():
    jatekos = [10, 9, 3]
    gep = [10, 9]
    vart_eredmeny = "j vesztett"
    kapott_eredmeny = eredemeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


def r_gep21():
    print("gép elérte a 21 et a játékos nem teszt:")
    jatekos = [10, 6, 4]
    gep = [10, 11]
    vart_eredmeny = "j vesztett"
    kapott_eredmeny = eredemeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


def r_gep21_21kevesebblap():
    print("gép elérte a 21 et kevesebb lapbol teszt")
    jatekos = [10, 6, 5]
    gep = [10, 11]
    vart_eredmeny = "j vesztett"
    kapott_eredmeny = eredemeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


def r_tultoltes():
    print("Játékos tul lépte 21 teszt:")
    jatekos = [10, 9, 3]
    gep = [10, 9]
    vart_eredmeny = "j veszett"
    kapott_eredmeny = eredemeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")
teszt_esetek()