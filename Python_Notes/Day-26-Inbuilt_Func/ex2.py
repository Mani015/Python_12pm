
# filter with map



# print(list(map(lambda i:i**2,filter(lambda k : k > 10 ,range(1,20)))))

# [121, 144, 169, 196, 225, 256, 289, 324, 361]


f1 = list(filter(lambda k: k>10 , range(1,20)))
# print(f1)
# [11, 12, 13, 14, 15, 16, 17, 18, 19]    ------> This list is we have to the iterable of map


m1 = list(map(lambda i : i**2, f1))
# print(m1)
# [121, 144, 169, 196, 225, 256, 289, 324, 361]


# range(1,20)----> square ----> i want below 100 values


# map with filter


print(list(filter(lambda j : j<=100, map(lambda i : i**2,range(1,20)))))
# map values:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100,121, 144, 169, 196, 225, 256, 289, 324, 361]


# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
