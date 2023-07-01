a = 33
b = 200


# for i in range(10):
#     if i*i == 49:
#         pass
#         print(i*i)


import time

attempts = 4

chance = 0

while chance < attempts:
    password = int(input('Enter your password:'))
    if password==1234:
        print('screen is unlock')
        break
    chance+=1
else:
    print('sorry you are fail')
time.sleep(5)
print('you are try again')

