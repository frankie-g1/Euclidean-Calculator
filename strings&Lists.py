import copy

el = list('Hello')
print(el)
# Alot of the same operations can be done on both strings and lists

name = 'Zophie'
#Z
print(name[0])
#op, not oph. EX: [1, 3)
print(name[1:3])
#i
print(name[-2])
#Zo
print('Zo' in name)
#Zophie, bad var name below
for abc in name:
    print(abc)  # or letter over abc

# Main difference is strings are immutable, i.e. cannot be changed but can be reassigned

# Can access letters in a string, but cannot reassign the letter

# Create new string using slices
#Below, its name[0, 7), which stops before a. name[8...) includes index 8. Index 12 DNE
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
#Now both spam and cheese index 1 = 'Hello!'
cheese[1] = 'Hello!'
#Prints 'Hello!'
print(spam[1])


def eggs(some_parameter):
    some_parameter.append('Hello')
    # someParameter refers to the spam reference


spam = [1, 2, 3]
eggs(spam)
print(spam)

cheese = copy.deepcopy(spam)
# creates new reference and new list
# Modifying cheese won't modify spam now

print('Four score and seven' + \
      ' years ago')
