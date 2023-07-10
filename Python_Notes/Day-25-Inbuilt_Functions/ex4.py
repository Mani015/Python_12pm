

def New(i):
    return i

names = 'vishal dhamu dinesh somu'

m2 = list(map(New,names.upper()))
# print(m2)
# ['V', 'I', 'S', 'H', 'A', 'L', ' ', 'D', 'H', 'A', 'M', 'U', ' ', 'D', 'I', 'N', 'E', 'S', 'H', ' ', 'S', 'O', 'M', 'U']


# using lambda

# print(map(lambda i:i**2,range(1,20)))
# <map object at 0x000001F80DE3B760>

print(list(map(lambda i:i**2,range(1,20))))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

print(set(map(lambda i : i ,'python developer'.upper())))
# {'L', 'H', 'D', 'E', 'O', 'P', 'V', 'Y', 'R', 'N', 'T', ' '}
