
# If statement inside another
# A nested if statement is an if statement that is nested (meaning, inside) another if statement or if/else statement.
# nested if-else: a if inside of another if is called nested if


# So the first approach has us place an if statement inside another. Here’s how that looks:
#
# if conditionA:
#     # Code that executes when 'conditionA' is True
#
#     if conditionB:
#         # Code that runs when 'conditionA' and
#         # 'conditionB' are both True



# how does it working

# Python evaluates this nested if statement when the condition of the preceding if statement is True.
# When conditionA is False, our nested if statement never runs. That happens even when its own condition is True.



# if 2>3:
#     print(True)
#
# else:
#     print(False)


a = int(input('Enter one number:'))
# 12
if 20>=a:
    print('1 st if condition is True')
    if 10>=a:
        print('2nd if true')
        if 5>=a:
            print('3rd if is true')
        else:
            print('3rd else is false')
    else:
        print('2nd else is fail')
else:
    print('1st else is fail')

# Enter one number:8
# 1 st if condition is True
# 2nd if true
# 3rd else is false
