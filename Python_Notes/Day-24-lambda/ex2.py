
l1 = []
for i in range(1,9): # iterable
    if i>5: #condition
        l1.append(i) #expression
# print(l1)
# [6, 7, 8]
# List Comprehension
# syntax:[expression iterable condition]

# print([i for i in range(1,9) if i>5])

# [6, 7, 8]


# if else list comprehension

l2 = [i if i%2==0 else i+1 for i in range(1,11)]
print(l2)
# [2, 2, 4, 4, 6, 6, 8, 8, 10, 10]
