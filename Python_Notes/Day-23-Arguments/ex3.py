def name(firstname,middlename,lastname):
    print('firstname is :',firstname)
    print('middlename is :',middlename)
    print('lastname is :',lastname)

# name(lastname='jakir',firstname='mani anna',middlename='Grk')
# firstname is : mani anna
# middlename is : Grk
# lastname is : jakir




def Fun(x,y,z):
    print()
    print('x value is :',x)
    print('y value is :',y)
    print('z value is :',z)

x = 10
y = 20
z = x+y
print()
print('z value is :',z)
x = x-y
print('x value is :',x)
y = z-x
print('y value is :',y)


Fun(y=z,z=x,x=y)
# x value is : 40
# y value is : 30
# z value is : -10
