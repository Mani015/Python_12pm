

def New_Fun(x1,x2):

    y1 = x1
    y2 = x2

    return 'addition of ', y1 + y2

# print(New_Fun(2,3))
# ('addition of ', 5)



# To assingning the new variable


def Old_Fun(a,b):
    a1 = a
    b1 = b

    c1 = a1 + b1

    return c1   # value of c1 is 9

# print(Old_Fun(4,5))
# New variable name
v1 = Old_Fun(4,5)
print('Table of :',v1)
# 9


for i in range(1,11):
    print(f'{v1} x {i} = {v1*i}')


# Table of : 9
# 9 x 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45
# 9 x 6 = 54
# 9 x 7 = 63
# 9 x 8 = 72
# 9 x 9 = 81
# 9 x 10 = 90
