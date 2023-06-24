
#  dict.setdefault(key,default= “None”)	set the key to the default value if the key is not specified in the dictionary

y1 = {1:'vishal',2:'sridhar',3:'bhaskar',4:'vinod',5:'jakir'}

y1.setdefault('int',123)
print(y1)
# {1: 'vishal', 2: 'sridhar', 3: 'bhaskar', 4: 'vinod', 5: 'jakir', 'int': 123}

print(y1.get('int'))

