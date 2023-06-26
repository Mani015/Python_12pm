
# update()	Updates the dictionary with the elements from another dictionary
# syn: dict.update(dictionary)

x1 = {1:'sudheer',2:'manoj',3:'rajan',4:'dhamu',5:'santhosh'}
x2 = {6:'sridhar',7:'vinod'}
# adding two dictionary
x1.update(x2)
print(x1)

# {1: 'sudheer', 2: 'manoj', 3: 'rajan', 4: 'dhamu', 5: 'santhosh', 6: 'sridhar', 7: 'vinod'}

# 8:'ramu'

x1.update({8:'ramu'})
print(x1)
# {1: 'sudheer', 2: 'manoj', 3: 'rajan', 4: 'dhamu', 5: 'santhosh', 6: 'sridhar', 7: 'vinod', 8: 'ramu'}
