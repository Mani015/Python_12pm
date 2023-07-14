
x = 00
def fool():
    x = 1
    print('l v:',x)
# print('g v:',x)
# fool()
# print('g v:',x)

# g v: 0
# l v: 1
# g v: 0


#  I am trying to update the global value using global keyword

y = 0
print('g v:',y)

def New_Fun():
    global y
    y = 12
    print('l v:',y)
    print('g l :',globals()['y'])
print('g v:',y)
New_Fun()


# g v: 0
# g v: 0
# l v: 12
# g l : 12