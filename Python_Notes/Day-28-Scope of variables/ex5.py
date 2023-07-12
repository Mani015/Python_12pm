# Rules of GLBE:


# local scope

def Local():
    x1 = 20
    print('local variable:',x1)
# Local()
# local variable: 20


non = 'python'

def Outer_fun():
    non1 = 'mysql'

    def Inner_fun():
        l1 = 'developer'
        print('local v:',non)

    Inner_fun()

Outer_fun()
