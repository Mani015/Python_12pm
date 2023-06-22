x2 = [1,2,3,4,[2,3,4,5,6,[22,33,44,55,66,77,88,99],[1,2,3,4,5,6,7,8,[11,22,33,44,55,66,77,88,99,100,22,54,69,85,7,4],'python','developer','java',
                ['main'],123,456,789,123,[23,45,67,89,00],'dinesh','vishal','saikairan','narendra','jitjendra'],11],11,22]


print(x2[3:10:2])
# print(x2[3][5][-10::-2])
# print(x2[10][-1][-2:])
# print(x2[3][6][8])
# [4, 11]
# TypeError: 'int' object is not subscriptable
# print(x2[90])

x2.remove(100000)
print(x2)
