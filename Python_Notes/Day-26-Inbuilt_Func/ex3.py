from functools import reduce
# reduce fucntion name is not here!
# we need to import from functools Moduls


# Reduce:
# syntax: reduce (functionName,Iterable)
x = [1,2,3,4,5,6,7,8,9,10]
# print(sum(x))
#55
# def New_Sum(x,y):
#     return x + y
#
# r1 = reduce(New_Sum,x)
# print(r1)
# 55




# multiplication of 1st 10 integers

def New_Sum(x,y):
    return x * y

r1 = reduce(New_Sum,x)
# print(r1)
# 3628800


