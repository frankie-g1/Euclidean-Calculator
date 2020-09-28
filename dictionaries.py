import pprint

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
sent = 'My cat has ' + myCat['color'] + ' fur.'
spam = {12345: 'Luggage combination', 42: 'The Answer'}

list(spam.keys())
list(spam.values())
spam.keys()

for k in spam.keys():
    print(k)


for k in spam.values():
    print(k)

#Both below avoid error messages, never assume a key exists because it will crash the script
if 'color' in myCat:
    print(myCat['color'])

#If color key does not exist, return zero
myCat.get('color', 0)

myCat.get('size', '')

picnic = {'apples': 5}
print('I am bringing ' + str(picnic.get('apples', 0)) + ' apples to the picnic')
#Instead of
print('I am bringing ' + str(picnic['apples']) + ' apples to the picnic')

myCat.setdefault('color', 'black')
#Below
#Does do something if there is no key (adds key and value) or no found value to a key (adds value)
#Doesn't do anything if key and value exist
myCat.setdefault('apples', 'orange')
print(myCat['apples'])

#Dictionary on K:V =  character, number of times in sentence
message = 'A practical programming course for office workers, academics, and administrators who want to improve their productivity. '
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character]+1

pprint.pprint(count)
#Returns string value
text = pprint.pformat(count)

#No first value in a dictionary unlike a list.




#Don't start with an IF if you are starting with an empty dictionary where if cases are not necessary
#Try to be more brute force when starting off on an objective
#Main reason I failed was using __setattr__, it would be on an object attribute such as length or class attributes
def use_count(message):

    for character in message:
        if count.get(character) is None:
            count.setdefault(character, 0)
        else:
            count[character] = count[character]+1


use_count(message)





