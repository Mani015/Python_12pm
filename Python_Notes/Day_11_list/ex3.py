# list is a mutable datatype
# what is mutable (A datatype it change any where , add/remove/update)
# remove()	Removes the item with the specified value

animals = ['lion','deer','elephant','tiger','leopard','ant','dog','cat','fox']
print(animals)
# syn: list.remove(value)
animals.remove('ant')
# ['lion', 'deer', 'elephant', 'tiger', 'leopard', 'ant', 'dog', 'cat', 'fox']
print(animals)
# ['lion', 'deer', 'elephant', 'tiger', 'leopard', 'dog', 'cat', 'fox']

animals.remove('fox')
print(animals)
# ['lion', 'deer', 'elephant', 'tiger', 'leopard', 'dog', 'cat']
animals.remove('tiger')
print(animals)
# ['lion', 'deer', 'elephant', 'leopard', 'dog', 'cat']

# animals.remove('snake')
# print(animals)
# ValueError: list.remove(x): x not in list

animals.remove()
print(animals)
# TypeError: list.remove() takes exactly one argument (0 given)
