# Enclosing Scope


t1 = 10
def Test1():
    # t1 = 30
    # print('non local variable:',t1)
    def Test2():
        t2 = 40
        print('local variable :',t2)
    Test2()
    print('non local variable:',t1)
Test1()

# NameError: name 't1' is not defined
# local variable : 40