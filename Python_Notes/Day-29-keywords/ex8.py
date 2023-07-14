
# x1 = 1
# print('g v:',x1)
# def Chandrayan_3(num):
#     global x1
#     x1 = 2+num
#     print('enclosing v:',x1)
#     def Chandrayan_2():
#         global x1
#         x1 = 3+num+2
#         print('l v:',x1)
#
#     Chandrayan_2()
#     print('En v:',x1)
# Chandrayan_3(3)
# print('g v:',x1)

# g v: 1
# enclosing v: 5
# l v: 8
# En v: 8
# g v: 8



x1 = 1
print('g v:',x1)
def Chandrayan_3(num):
    global x1
    x1 = 2+num
    print('enclosing v:',x1)
    def Chandrayan_2():
        global x1
        x1 = 3+num+2
        print('l v:',x1)
    print('enclosing v:', x1)
    Chandrayan_2()
    print('En v:',x1)
Chandrayan_3(3)
print('g v:',x1)


# g v: 1
# enclosing v: 5
# enclosing v: 5
# l v: 8
# En v: 8
# g v: 8




















