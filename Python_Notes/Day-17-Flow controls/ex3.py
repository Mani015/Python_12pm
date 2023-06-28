# Find out the percentage of student:


lan1 = int(input('enter lan1 marks:'))
lan2 = int(input('enter lan2 marks:'))
english = int(input('enter english marks:'))
maths = int(input('enter maths marks:'))
science = int(input('enter science marks:'))
social = int(input('enter geography marks:'))

totalmarks  =  lan1+lan2+english+maths+social+science
print('total marks of all subjects:',totalmarks)

percentage = (totalmarks/600)*100

print('student percentage:',percentage)


# enter lan1 marks:99
# enter lan2 marks:89
# enter english marks:85
# enter maths marks:100
# enter science marks:97
# enter geography marks:95
# total marks of all subjects: 565
# student percentage: 94.16666666666667
