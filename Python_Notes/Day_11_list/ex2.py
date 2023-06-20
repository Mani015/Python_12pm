# copy()	Returns a copy of the list
Lt = ['hp','dell','apple','asis','lenovo','realme','dell1','samsung','redme']

# print(Lt)
# ['hp', 'dell', 'apple', 'asis', 'lenovo', 'realme', 'dell1', 'samsung', 'redme']

lt2 = Lt.copy()
print(lt2)
# ['hp', 'dell', 'apple', 'asis', 'lenovo', 'realme', 'dell1', 'samsung', 'redme']


print(lt2 is Lt)
# False

lt2 = Lt
print(lt2 is Lt)
# True