
#  i did not declare the global variable name


def Atom():
    global x
    x = 10
    print('l v:',x)
# Atom()
# print('g v:',x)
# l v: 10
# g v: 10



v1 = 0
print('g v:',v1)

def Fun(value):
    print('g v :',v1)
    def Joy():
        global v1
        v1 = 20
        print('local v:',v1)
    Joy()
    print('g v :',v1)
Fun(2)
print('g v:',v1)
# g v: 0
# g v : 0
# local v: 20
# g v : 20
# g v: 20
