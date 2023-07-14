# Reversing the Mobile Number
# x=eval(input("enter mobile number:"))
# r=0
# while x > 0:
#     m = x%10
#     r = (r*10)+m
#     x = x//10
# print(r)

x1 = 1
print('g v:',x1)
def Chandrayan_3():
    global x1
    x1 = 2
    print('enclosing v:',x1)
    def Chandrayan_2():
        x1 = 3
        print('l v:',x1)
    Chandrayan_2()
    print('En v:',x1)
Chandrayan_3()
print('g v:',x1)

# g v: 1
# enclosing v: 2
# l v: 3
# En v: 2
# g v: 2
