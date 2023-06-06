# OR Denoted By pipe Symbol ' | '
# 10|20
# 13|18
# 19|88
# 16|97

print(True | True)
# True
print(False | True)
# True
print(True | False)
# True
print(False | False)
# False


print(10 | 20)
# 10 : 0  0  0  0  1  0  1  0
# 20 : 0  0  0  1  0  1  0  0
# --------------------------------
#(|) : 0  0  0  1  1  1  1  0
# 30

print(13|18)
# 31

print(19|88)
# 91

print(16|97)
# 113

print(12 | 18 | 30)
# 30

