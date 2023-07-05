
def Main_Fun(x):

    if x>10:
        def f1():
            print(True)
        f1()
    else:
        def f2():
            print(False)
        f2()

x = int(input('Enter one number:'))
Main_Fun(x)