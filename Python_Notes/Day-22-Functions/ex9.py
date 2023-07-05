
# Types of arguments:
# 1). postional Arguments
# 2).Keyword Arguments
# 3).Default Arguments
# 4).Variable lenth (orbitary) Arguments


# Positional Arguments in Python
# During a function call, values passed through arguments should be in the order of parameters in the function
# definition. This is called positional arguments.
#
# Keyword arguments should follow positional arguments only.
#
# def add(a,b,c):
#     return (a+b+c)


def f1(a,b):
    print(a,b)
f1(1)

# TypeError: f1() missing 1 required positional argument: 'b'
