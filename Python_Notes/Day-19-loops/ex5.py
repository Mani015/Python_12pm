

# I want first 10 numbers which are divisible by 7 and 9


k = 0

x = 1

while k<10:
    if x%7==0 and x%9==0:
        k+=1
        print('this number divisible by 7 and 9:',x)
    x+=1
print('loop completed')