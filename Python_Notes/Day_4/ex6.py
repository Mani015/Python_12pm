# BITWISE OPERATOR:
# &,|,^,<<,>>,~

# &

a = 10
b = 20
print( a & b)
# 0

print(True & True)
# True
print(True & False)
# False
print(False & True)
# False
print(False & False)
# False

# a = 10   0 1 0 1 0
# b = 20   1 0 1 0 0
# ----------------------
#  a & b = 0 0 0 0 0


print(16 & 32)
# 0
print(19 & 52)
# 16
print(21 & 30)
# 20
print(57 & 99)
# 33
