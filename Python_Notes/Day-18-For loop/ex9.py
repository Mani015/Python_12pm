x3 = []
for i in range(1,11):
    if i%2==0:
        x3.append(i)
    else:
        x3.append(i+1)
print(x3)

# [2, 2, 4, 4, 6, 6, 8, 8, 10, 10]

# To remove the duplicate values in list

print(set(x3))
# {2, 4, 6, 8, 10}

print()

for i in range(1,6):
    print('square of:',i*i)

#square of: 1
# square of: 4
# square of: 9
# square of: 16
# square of: 25
