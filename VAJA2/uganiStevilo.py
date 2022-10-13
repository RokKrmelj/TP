import random


st = 5
x = random.randrange(0, 31)
while(st > 0):
    print("preostali poiskusi: " + str(st))
    ugib = input('vpiši število od 1 do 30: ')
    if(str(ugib) < str(x)):
        print("prenizko")
    elif(str(ugib) > str(x)):
        print("previsoko")
    else:
        print("zmaga! pravilno število je: " + str(x))
        st = 0
    
    st = st - 1
if st == 0:
    print("zmanjkalo poiskusov")