
# Global Variable:
# global variable is a variable , that variable is declared out side of the function, we can use any where

x1 = 100
print('global variable :',x1)

def Main():
    x2 = 200
    print('Local variable:',x2)
    print('Global variable:',x1)
Main()
print('Global variable:', x1)

# global variable : 100
# Local variable: 200
# Global variable: 100
# Global variable: 100
