def max_(x, y, z):

    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    else:
        print(z)

max_(10000, 99, 999)