

x = int(input('Enter one number:'))


def Outer():
    if x == 10:
        def New():
            print('equals to 10')
    else:
        def New():
            print('not equal to 10')
    return New()


Outer()
