
# To find out Consonants


def Consonants(C):
    if C not in 'aeiou':
        return True

st1 = input('Enter one string:')

# Con = tuple(filter(Consonants,st1))
# print(Con)
# Enter one string:zero is better than copy
# ('z', 'r', ' ', 's', ' ', 'b', 't', 't', 'r', ' ', 't', 'h', 'n', ' ', 'c', 'p', 'y')


# using lambda :

print()
print(tuple(filter(lambda Con : Con not in 'bcdfghjklmnpqrstvwxyz',st1)))
# ('a', ' ', 'e', ' ', 'a', 'e', ' ', 'a', 'e', ' ', 'u')


# print(list(filter(lambda x: x not in 'aeiou','abcdefghijklmnopqrstuvwxyz')))