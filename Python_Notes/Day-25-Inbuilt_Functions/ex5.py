# filter


#
# The filter() function in Python is another built-in function that, similar to map(),
# operates on an iterable. However, instead of applying a function to each item and returning the results,
# filter() applies a function to each item and returns an iterator containing only the items for which the function returns True.


# syntax:filter(functionName,iterable)

def Positve_numbers(postive):
    if postive > 0:
        return True

num = (1,3,-5,-3,5,6,-12,-3,-4,-23,45,67)

f1 = filter(Positve_numbers,num)
print(list(f1))
# [1, 3, 5, 6, 45, 67]



# using lambda:


# reduce(functionname,iterable)


