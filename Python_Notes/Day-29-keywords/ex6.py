


v1 = 0
def Fun(value):
    print('g v :',v1) # 0
    def Joy():
        global v1
        v1 = v1+value
        print('local v:',v1)

    print('g v :', v1)
    Joy()
    # print('g v :',v1)
Fun(2)
print('g v:',v1)

# g v : 0
# local v: 2
# g v : 2
# g v: 2
