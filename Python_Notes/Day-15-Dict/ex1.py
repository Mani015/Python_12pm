
x1 = {1:'sudheer',2:'manoj',3:'rajan',4:'dhamu',5:'santhosh'}
# print(x1)
# {1: 'sudheer', 2: 'manoj', 3: 'rajan', 4: 'dhamu', 5: 'santhosh'}


# pop()	Returns and removes the element with the given key
# syn: dict.pop(key)
x1.pop(2)
print(x1)
# {1: 'sudheer', 3: 'rajan', 4: 'dhamu', 5: 'santhosh'}

x1.pop(5)
# print(x1)
# {1: 'sudheer', 3: 'rajan', 4: 'dhamu'}

x1.pop(6)
print(x1)
# KeyError: 6