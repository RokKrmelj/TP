praštevilo = False

for i in range(51):
    if(i > 1):
        praštevilo = True
        for j in range(2, i):
            if((i % j) == 0):
                praštevilo = False
                break
        if praštevilo:
            print(i)

