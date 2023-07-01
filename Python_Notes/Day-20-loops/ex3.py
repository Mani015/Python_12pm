

# Python continue Statement
# The continue statement is used to skip the current iteration of the loop and the control flow of the program goes to the next iteration.
#
# The syntax of the continue statement is:


names = ['dhamu','sridhar','shiva','jithendre','vinod','saikiran','narendra']
# for i in names:
#     print(i,end=' ')
# dhamu sridhar shiva jithendre vinod saikiran narendra

# I don't want vinod'

for i in names:
    if i=='vinod':
        continue
    print(i)
# dhamu
# sridhar
# shiva
# jithendre
# saikiran
# narendra

