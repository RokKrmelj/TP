import requests

iskalniNiz = input("Vpiši iskalni niz: ")
iskanje = requests.get('https://www.rtvslo.si/iskalnik?q=' + str(iskalniNiz))
print(iskanje.text)