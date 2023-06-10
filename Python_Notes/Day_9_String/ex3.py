# replace(oldname,newname)
x1 = 'dinesh java Developer vishal java developer bhaskar java developer'

print(x1)
print()
# dinesh java Developer vishal java developer bhaskar java developer

print(x1.replace('java','python'))
# dinesh python Developer vishal python developer bhaskar python developer
# replace(oldname,newname,count)
# print(x1.replace('java','Frontend',1))
# dinesh Frontend Developer vishal java developer bhaskar java developer
print()
print(x1.replace('java','backend',-2))
# dinesh backend Developer vishal backend developer bhaskar java developer


# print(x1.replace('java','backend',4))
# dinesh backend Developer vishal backend developer bhaskar backend developer


# print('dinesh java Developer vishal java developer bhaskar java developer'.replace('java','testing',-2))

# print('tomoto'.replace('t','z','tomoto'[-2]))
