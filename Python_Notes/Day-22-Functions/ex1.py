

def fun(x):

    for i in range(1,11):
        print(f'{x} x {i} = {x*i}')   # using formate string
        # print(x , 'x', i, '=', x*i)

fun(x=int(input('Enter one number:')))

# Enter one number:4
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 4 x 10 = 40
