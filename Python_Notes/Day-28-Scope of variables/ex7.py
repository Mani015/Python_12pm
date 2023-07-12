
# Global Scope:

z1 = 100
def Test1():
    # t1 = 30
    # print('non local variable:',t1)
    def Test2():
        t2 = 40
        print('local variable :',z1)
    Test2()
    # print('non local variable:',z1)
Test1()
print('global v:',z1)
# local variable : 100
# global v: 100


