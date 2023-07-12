
g1 = [1,2,3,4,5,6,7]

def OuterFun():
    g2 = [3,4,5]
    # g3 = 20
    print('global v:',g1)
    print('local of :',g2)
    def Inner_Fun():
        g3 = 23
        print('local v:',g3)
        print('Sum of global variable:',sum(g1))
    Inner_Fun()
    print('length of the non-local variable:',len(g2))
OuterFun()

