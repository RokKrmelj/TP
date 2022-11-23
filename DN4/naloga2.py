import math

dolzinaSeznama = int(input("Vnesi dolžino seznama: "))

seznam = [0] * dolzinaSeznama

for i in range(0, dolzinaSeznama):
    seznam[i] = int(input("Vnesi število: "))
    i = i + 1

seznamMin = min(seznam)
seznamMax = max(seznam)
seznamPovprečje = int(math.fsum(seznam)/len(seznam))
seznamBlizuPovprečja = min(seznam, key = lambda x: abs(seznamPovprečje - x))

print("Najmanjša vrednost: " + str(seznamMin))
print("Največja vrednost: " + str(seznamMax))
print("Povprečna vrednost: " + str(seznamPovprečje))
print("Vrednost najbližja povprečju: " + str(seznamBlizuPovprečja))