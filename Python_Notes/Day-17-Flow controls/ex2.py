
# Assigning a letter grade based on a numerical score
#  35 to 50 4th Grade
# 51 to 65 3th Grade
# 66 to 75 2nd Grade

# 76 to 100 1st Grade

# below 45 you are fail


a=int(input("enter your marks:"))
if(a>=76):
    print("1st grade")
elif(a>=66):
    print("2nd grade")
elif(a>=51):
    print("3rd grade")
elif(a>=35):
    print("4th grade")
else:
    print("fail")
