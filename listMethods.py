spam = ['hello', 'loud', 'loud', 'hungry']
spam.index('hello')
#Output 0

#spam.index('exception')
#Will raise value error exception

spam.append('moose')
#Adds a value to the end of this list

spam.insert(1, 'There!')
#Adds an item to a specific index

spam.remove('loud')
#Value error if object DNE within spam.
#Removes only 1 instance of loud

del spam[0]
#Different, del only deletes index and not a value

nums = [3.14, 18, 99, 88, 91]
nums.sort()
nums.reverse()
nums.sort(reverse=1)
spam.sort(key=str.lower)
print(spam)
print(nums)