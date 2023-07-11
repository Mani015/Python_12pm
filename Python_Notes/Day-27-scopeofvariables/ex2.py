
# Local variable: A local variable is variable , that variable declared in side of the function is
# called local varaible

def Test():
    x1 = 10
    print('local variable :',x1)
# Test()
# local variable : 10


# Scope of  local variable
# local variable is variable , only we can use(call) inside of the fuction, we can't call the oust of the function

def New():
    x2 = 20
    print('local variable :',x2)
New()
# local variable : 20
# if i am trying to call the local variable out side of th function
print('local variable :',x2)
# NameError: name 'x2' is not defined
