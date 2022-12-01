# uvozimo knjižnico
import requests
import time

# naredimo spremenljivko, v kateri je shranjen URL do API-ja
BASE_URL = "https://api.rtvslo.si"

def get_api_data(url_path):
    # ustvarimo GET klic na API
    response = requests.get(f"{BASE_URL}{url_path}")
    # podatke vrnjene v JSON formatu pretvorimo v Python slovar
    return response.json()


danasnjiDatum = time.strftime("%Y-%m-%d")
print("Vnesite želeno postajo (tvs1, tvs2, tvs3, tvkp, tvmb, tvmmc, ra1, ra2, ra3, prvi, val202, ars, rakp, ramb, capo)")
postaja = input("Postaja: ")



# pokličemo funkcijo za izbrano postajo
dnevniSpored = get_api_data(f"/spored/list/{postaja}/{danasnjiDatum}")
print(f"****** Spored za {postaja} ******")
# izluščimo želene podatke iz slovarja
stProgramov = (len(dnevniSpored["response"])-1)
for i in range(stProgramov):
    print(dnevniSpored["response"][i]["ura"] + " " + dnevniSpored["response"][i]["vsebina"])