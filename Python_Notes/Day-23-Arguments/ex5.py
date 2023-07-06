

# def Main(x=10,y=20,z=30):
#     print('x value is :', x)
#     print('y value is :', y)
#     print('z value is :', z)
#
# Main(12,14,16)
# x value is : 12
# y value is : 14
# z value is : 16

# for example , will update only  y value , using keyword arguments

def Main(x=10,y=20,z=30):
    print('x value is :', x)
    print('y value is :', y)
    print('z value is :', z)

Main(y=14)

# x value is : 10
# y value is : 14
# z value is : 30
