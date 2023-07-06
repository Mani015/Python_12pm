

# For arbitrary positional argument, an asterisk (*) is placed before a parameter in function definition
def New_fun(*py):
    x = py
    print(x)
# New_fun(1,2,3,4,5,6,7,8,9,0,10,11,2,33)


def New_Addtition(*java):
    x = list(java)

    print(sum(x)**2)
New_Addtition(1,2,3,4,5,6,5,6,45,9)
# 86


