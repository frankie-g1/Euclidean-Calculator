#comma delimited elements of any type
#['cat', 'bat, 'rat', 'elephant']
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
print(spam[0])
print()

print('Spam 2 next')
spam2 = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam2[1][4])
#-2 denotes second to last list within the list
#-1 would denote the last list
#0 denotes the first list
#negatives denote from the last, -1 is last, -2 is second to last, -3 throws an index out of range error
print(spam2[-2])
print()


# A slice is a portion of a list
print("Slice made from spam 1")
exo = spam[1:3]
print(exo)
print()

#Modifying a list
print("Modifying a list")
print("Original spam:", list(spam))
spam[0] = 80
print(list(spam))
#Add in elements when adding in a slice, number of elements added are denoted after the equal sign, Index 4 does not exist after the executed code below
spam[1:4] = ['Mouse', 'Moose', 'Truck']
print(spam)
print()


#slice shortcuts
#spam[:2] means start at the beginning and stop but not including the 2 index
#spam[1:] start at index 1 and return the rest of the list
#del spam[2] and that index gets deleted from the list, doesn't leave any gaps in the list
print("Del practice, an unassign keyword")
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
#rat goes away
print(spam)


#len function
len('Hello') #5
len([1,2,3]) #3
'Hello' + 'world'
[1,2,3] + [4,5,6]
[1,2,3] * 3
list('Hello')

'howdy' in ['hello', 'hi', 'howdy'] # evaluates to true
'howdy' not in ['hello', 'hi', 'howdy'] # evaluates to false