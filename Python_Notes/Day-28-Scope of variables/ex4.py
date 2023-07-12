
g1 = [1,2,3,4,5,6,7]

def OuterFun():
    g2 = [3,4,5]
    print('global v:',g1)
    print('local of :',g2)
    def Inner_Fun():
        g3 = 23
        print('local v:',g3)
        print('Sum of global variable:',sum(g1))
    Inner_Fun()
    print('length of the non-local variable:',len(g2))
OuterFun()

# global v: [1, 2, 3, 4, 5, 6, 7]
# local of : [3, 4, 5]
# local v: 23
# Sum of global variable: 28
# length of the non-local variable: 3
