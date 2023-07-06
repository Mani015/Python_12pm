
# Arbitary keyword Argumets
# ARBITRARY KEYWORD ARGUMENTS IN PYTHON
# For arbitrary positional argument, a double asterisk (**) is placed before a parameter in a function
# which can hold keyword variable-length arguments.

def new_Dict(**dict):
    print(dict)

# new_Dict(a=10,b=20,c=30,d=40)



def Main_Dict(**vishal):
    for i in vishal.items():
        print(i)

Main_Dict(s1 = 'dhamu',s2='vishal',s3='madhu',s4='jajir')
# ('s1', 'dhamu')
# ('s2', 'vishal')
# ('s3', 'madhu')
# ('s4', 'jajir')
# syntax: lambda argumets : expression
a=10
b =20

print(a+b)
# 30
print((lambda a,b:a+b)(a,b))
