data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}
def najvecja_vrednost(podatki):
    i = 0
    najvecjaVrednost = [0,0] 
    for key in podatki:
        najvecjaVrednost[i] = max(podatki[key])
        i = i + 1
    return najvecjaVrednost