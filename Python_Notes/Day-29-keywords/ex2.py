
# x = 0
def Fun():
    x = 2
    print('local v:',x) #local v: 2

# print(x) NameError: name 'x' is not defined
# Fun()





y = 0

def Key(x):

    print(x)
# print(x)
print('global v:',y)
Key(2)

# global v: 0
# 2
