

# Nested Function: A function , inside another function is called nested function

def OuterFunction():
    x = 10
    y = 20
    def InnerFunction():
        print(x + y)

    InnerFunction()
OuterFunction()

# 30


