# megoldas

def pontszamitas(lapok):
    ertek = 0
    for i in range(len(lapok)):
        ertek += lapok[i]
    return ertek


def eredemeny(jlapok, geplapok):
    gep = pontszamitas(geplapok)

    j = pontszamitas(jlapok)

    if j <= 21 or gep <= 21:
        if j > gep:
            s = "j nyert"
        elif gep > j:
            s = "gep nyert"
        elif j == gep:
            if len(jlapok) < len(geplapok):
                s = "j nyert"
            elif len(jlapok) > len(geplapok):
                s = "gep nyert"
            else:
                s = "döntetlen , osztoztok a nyereségen"
    elif j > 21:
        s = "j vesztett"
    elif gep > 21:
        s = "gep vesztett"
    elif j > 21 and gep > 21:
        s = "döntetlen haz nyert"
    print(s)
    return s

    # teszt esetek


def teszt_esetek():
    jatekos_vesztett_teszt()
    r_gep21_teszt()
    r_gep21_21kevesebblap_teszt()
    r_tultoltes_teszt()
    konkret_dontetlen_teszt()
    lapok_összege_g_kisseb_21_teszt()
    lapok_összege_j_kisseb_21_teszt()
    nagyobb_nyer_teszt()
    nagyobb_nyer2_teszt()


def jatekos_vesztett_teszt():
    jatekos = [10, 9, 3]
    gep = [10, 9]
    vart_eredmeny = "gep nyert"
    kapott_eredmeny = eredemeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


def r_gep21_teszt():
    print("gép elérte a 21 et a játékos nem teszt:")
    jatekos = [10, 6, 4]
    gep = [10, 11]
    vart_eredmeny = "gep nyert"
    kapott_eredmeny = eredemeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


def r_gep21_21kevesebblap_teszt():
    print("gép elérte a 21 et kevesebb lapbol teszt")
    jatekos = [10, 6, 5]
    gep = [10, 11]
    vart_eredmeny = "gep nyert"
    kapott_eredmeny = eredemeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


def r_tultoltes_teszt():
    print("Játékos tul lépte 21 et teszt:")
    jatekos = [10, 9, 3]
    gep = [10, 9]
    vart_eredmeny = "j veszett"
    kapott_eredmeny = eredemeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


def lapok_összege_g_kisseb_21_teszt():
    print("gep_kevesebb 21 nel")
    jatekos = [10, 9, 2]
    gep = [10, 9]
    vart_eredmeny = "gep veszett"
    kapott_eredmeny = eredemeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


def lapok_összege_j_kisseb_21_teszt():
    print("j_kevesebb 21 nel")
    jatekos = [10, 2, 2]
    gep = [10, 9]
    vart_eredmeny = "j veszett"
    kapott_eredmeny = eredemeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


def nagyobb_nyer_teszt():
    print("gep nagyobb mint jatekos")
    jatekos = [10, 2, 2]
    gep = [10, 9]

    kapott_eredmeny = eredemeny(jatekos, gep)
    if gep > jatekos:
        vart_eredmeny = "j veszett"
    if kapott_eredmeny == vart_eredmeny:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


def nagyobb_nyer2_teszt():
    print("gep kissebb mint jatekos")
    jatekos = [10, 2, 2]
    gep = [10, 9]
    vart_eredmeny1 = "j nyert"
    kapott_eredmeny = eredemeny(jatekos, gep)

    if kapott_eredmeny == vart_eredmeny1:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


def konkret_dontetlen_teszt():
    print("ugyan anyi lap, mind ketö teljesen egyenlöen vesztett vagy nyert")
    jatekos = [10, 9, 2]
    gep = [10, 9, 2]
    vart_eredmeny2 = "j vesztett"
    kapott_eredmeny = eredemeny(jatekos, gep)


    if kapott_eredmeny == vart_eredmeny2:
        print("a jatekos_vesztett teszt sikeres")
    else:
        print("a jatekos_vesztett teszt megbukott")


teszt_esetek()
