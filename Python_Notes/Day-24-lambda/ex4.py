
emp = ['Name','Age','Salary','id','location']
details = ['Vivek',26,100000,102, 'pune']

New_Dict = {}

for i,j in zip(emp,details):
    New_Dict[i] = j
print(New_Dict)

# {'Name': 'Vivek', 'Age': 26, 'Salary': 100000, 'id': 102, 'location': 'pune'}

# Dict Comprehension

# syn: {expression iterable condition}
# write down logic here.....

d1 = {i:i**2 for i in range(1,11) if i%2==0}
print(d1)
# {2:4,4:16,6:36,8:64,10:100}
