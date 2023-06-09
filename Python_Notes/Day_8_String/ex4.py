
# TO call with ending index

x2 = 'PYTHONISAGENERALPURPOSEPROGRAMMINGLANGUAGE'
# sytanx: string[start : end : step = 1]

print(x2[0:5])
# 0 is a starting index, 5 is a ending index
# PYTHO
# Logic inside :

# start<ending
#  0  <  5 -----> True -----> P
#  1  <  5------> True -----> Y
#  2  <  5 ------> True------> T
#  3  <  5 ------> True -----> H
#  4 <  5  ------> True -----> o
#  5  < 5 -----> Fasle

print(x2[2:9])
# THONISA
print(x2[1:16])
# YTHONISAGENERAL
print(x2[5:20])
# NISAGENERALPURP
print(x2[3*2 : 12])
# ISAGEN
print('show',x2[18:12])

print('x2 string taken of :',len(x2))
# x2 string taken of : 42

