
# Taking same variable name (local and global) but different values


x1 = 20
# print('global variable:',x1)

def Altroz():
    x1 = 30
    print('local variable:',x1)
    print('global variable:', x1)
# Altroz()
# print('global v:',x1)

# global variable: 20
# local variable: 30
# global variable: 30
# global v: 20


x1 = 20
print('global variable:',x1)

def Altroz1():
    # print('global variable:', x1)
    x1 = 30
    print('local variable:',x1)
Altroz1()
# UnboundLocalError: local variable 'x1' referenced before assignment