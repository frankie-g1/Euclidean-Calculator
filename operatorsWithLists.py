#For loops with lists below

for i in range (4):
    print(i)

#range(4)
#range(0,4), excluding 4
#python sees it as [0,1,2,3]

for i in [0,1,2,3]:
    print(i)

#returns an actual list [0,1,2,3]. (Instead of the sequence of range(4))
list(range(4))

#Creates a list of range 0 to excluding 100, and skips twice (only even numbers)
list(range(0, 100, 2))
print(list(range(0, 100, 2)))
spam = list(range(0, 100, 2))

range(len(spam))
#outputs: range(0, 50)
print(range(len(spam)))

for i in range(len(spam)):
    #str(i) and str(spam[i]) because Python cannot concatenate/'+' "Alicia" with 1980. Alicia + 1980 can't work, both aren't same type
    #+ concatenations only work when they are converted to str. If not, then commas are needed to append differing types
    print('Index',  (i), 'of spam is:', float(spam[i])) #numbers of any kind
    #OR
    print('Index '+  str(i), 'of spam is: '+ str(spam[i]))
    #COMMAS add a space, while straight up + str concatenation does not.

    #PS. Spam is a list of integers, if it was a list of strings, then print(...... + spam[i]) would work smoothly


#Multiple assignments
cat = ['fat', 'orange', 'loud', 'hungry']
size, color, disposition, disposition2 = cat
print(disposition2)


a = 'AAA'
b = 'BBB'
#NO MORE NEED for temp variables to switch!!!!!
a, b = b, a


#Augmented Assignment operators
number = 42
number += 1
#adds one, also can be done with any operation

