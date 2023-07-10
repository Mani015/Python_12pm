# using lambda
from functools import reduce

print(reduce(lambda a,b : a*b,range(1,11)))
# 3628800
# 1 is x , 2 is y , x +y = x
# x  = x+y == 1 + 2 = 3
# again is 3 is x , 3 is y


print(reduce(lambda a,b : a/b,range(1,11)))
# 2.7557319223985894e-07
