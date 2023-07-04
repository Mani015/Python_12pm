
#  find out prime numbers in list

x1 = [1,2,3,4,5,6,7,8,9,10,11,44,55,66,77,88,99]
#
x = False
y1 = []
for i in x1:
    for j in range(2,i):
        if i%j==0:
            x = True
            break
    else:
        y1.append(i)

print(y1)