
dict1 = {'fox':'animal','ball':'thing','banana':'fruit','mobile':'electronicdevice','vishal':'goodguy',
         'goodness':'searching for dhamu','python defination':'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.'}


# dict1.keys('fox')
# print(dict1)

print(dict1.get('fox'))
# animal
print(dict1.get('vishal'))
# goodguy
print(dict1.get('dhamu'))
# None

print(dict1.get('goodness'))
# searching for dhamu

print(dict1.get('python defination'))
# Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.
