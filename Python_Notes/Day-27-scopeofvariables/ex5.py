# How to get the global variable inside of function with same variable name
# we are using globals() method

x1 = 20
# print('global variable:',x1)

def Altroz():
    x1 = 30
    print('local variable:',x1)
    print('global variable:', globals()['x1'])

# Altroz()
# print('global v:',x1)
# global variable: 20
# local variable: 30
# global variable: 20
# global v: 20



# Adding the global and local using with same variable name
var1 = 10
def Addition():
    var1 = 20
    print('adding global + local:',var1 + globals()['var1'])
Addition()
# adding global + local: 30
print(locals()['var1'])