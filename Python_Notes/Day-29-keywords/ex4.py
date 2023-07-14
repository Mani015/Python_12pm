

# oldname = 'Vishal'
# print('g v--->1:',oldname)
#
# def NameChange():
#     newname = 'Vishal Kumar'
#     print('lv---->3:',newname)
# print('g v--> 2:',oldname)
# NameChange()
# g v--->1: Vishal
# g v--> 2: Vishal
# lv---->3: Vishal Kumar




oldname = 'Vishal'
print('g v--->1:',oldname)

def NameChange():
    global oldname #Vishal kumar
    oldname = 'Vishal Kumar'
    print('lv---->3:',oldname)
    print('--->',globals()['oldname'])

print('g v--> 2:',oldname)
NameChange()
print('g v ---> 4:',oldname)


# g v--->1: Vishal
# g v--> 2: Vishal
# lv---->3: Vishal Kumar
# g v ---> 4: Vishal Kumar


x = []
print('before list:',x)
for i in range(1,6):
    x.append(i)
print('after updating list:',x)
