

x = 10

x = 20
print(x)
#20

y = 20

def f1():
    y = 30
    print('inside function:',y)
# f1()
# print('outside of function:',y)
# inside function: 30
# outside of function: 20


def fun2():
    print('function')

for i in range(5):
    fun2()