def emso_leta_preracun():
    emso = input("vnesi svoj emšo: ")
    letoRojstva = emso[4:7]
    if (int(letoRojstva[0]) == 9):
        letoRojstva = int(letoRojstva) + 1000
    else:
        letoRojstva = int(letoRojstva) + 2000
        print("else")
    starost = 2022 - letoRojstva
    return starost