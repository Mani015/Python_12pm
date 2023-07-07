
# num = int(input('Enter one number:'))

# if num%2==0:
#     print(num,'even number')
# else:
#     print(num,'odd number')


# Enter one number:7
# 7 odd number


# print((lambda num : (num,'even number') if num%2==0 else (num,'odd numberr'))(num))
# <function <lambda> at 0x0000024793E9CD30>
# Enter one number:8
# (8, 'even number')


print((lambda num : (num,'even number') if num%2==0 else (num,'odd numberr'))(10))
# (10, 'even number')
