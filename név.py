#megoldas

def pontszamitas(lapok):
    ertek=0
    for i in range(len(lapok)):
        ertek+=lapok[i]
        return ertek
def eredemény(geplapok, jlapok):
    gep=pontszamitas(geplapok)
    j=pontszamitas(jlapok)
    if gep>21:
        print("gep vesztett")
    if  j>21:
        print("j vesztett")
#teszt esetek