

num = int(input('Enter one number:'))

if num > 1:
    for i in range(2,num):
        if num%i==0:
            print(num,'not a prime number')
            break
    else:
        print( 'is a prime number')


# Enter one number:12
# 12 not a prime number