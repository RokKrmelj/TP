import requests

iskalniNiz = input("Vpiši iskalni niz: ")
iskanje = requests.get('https://www.rtvslo.si/iskalnik?q=' + iskalniNiz)
print(iskanje.text)