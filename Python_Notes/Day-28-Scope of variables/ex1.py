
# Python Nonlocal Variables(Enclosing variable)
# In Python, nonlocal variables are used in nested functions whose local scope is not defined.
# This means that the variable can be neither in the local nor the global scope.


g1 = 'python'
print('global variable:',g1)

def Outer_fun():
    non = 'mysql'
    print('enclosing v:',non)
    def Inner_fun():
        l1 = 'developer'
        print('local v:',l1)
    Inner_fun()
Outer_fun()

# global variable: python
# enclosing v: mysql
# local v: developer
