g1 = 'python'
print('global variable:',g1)

def Outer_fun():
    non = 'mysql'
    print('enclosing v:',non)
    print('global variable:', g1)
    def Inner_fun():
        l1 = 'developer'
        print('local v:',l1)
        print('global variable:', g1)
    Inner_fun()
    print('global variable:', g1)
Outer_fun()
print('global variable:',g1)

# global variable: python
# enclosing v: mysql
# global variable: python
# local v: developer
# global variable: python
# global variable: python
# global variable: python
