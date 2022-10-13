
x = 5.1
y = 5

if (x < y):
    print("smo znotraj if")
    print(str(x) + " je manjše kot " + str(y))
    print("konec if")
elif (y == x):
    print("smo znotraj else if")
    print(str(x) + " je enako " + str(y))
    print("konec else if")
else:
    print("smo znotraj else")
    print(str(x) + " je večje kot " + str(y))
    print("konec else")
