# def max_(x, y, z):

#     if x > y and x > z:
#         print(x)
#     elif y > x and y > z:
#         print(y)
#     else:
#         print(z)

# max_(10000, 99, 999)

# 
def maxN_(x):
    a = 0
    for i in x:
        if i > a:
            a = i
    print(a)
    
    
x = (8,99,8,14,5,5,6,5,3,2,55,2,23,4,25,23532,5,3,4)

maxN_(x)

