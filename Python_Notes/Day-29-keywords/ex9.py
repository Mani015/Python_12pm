# Nonlocal

# you can make use of nonlocal,
# a keyword which functions very similarly to global, but primarily takes effect when nested in methods.
# nonlocal essentially forms an in-between of global and local scope.



# x = 10
# print('g v:',x)
#
# def M1():
#     x = 20
#     print('before e v:',x)
#     def M2():
#         x = 30
#         print('l v:',x)
#     M2()
#     print('after E v:',x)
# M1()

# g v: 10
# before e v: 20
# l v: 30
# after E v: 20





x = 10
print('g v:',x)

def M1():
    x = 20
    print('before e v:',x)
    def M2():
        nonlocal x
        x = 30
        print('l v:',x)
    M2()
    print('after E v:',x)
M1()

# g v: 10
# before e v: 20
# l v: 30
# after E v: 30
