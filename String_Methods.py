import sys

spam = 'Hello World!'
ex1 = spam.upper()
ex2 = spam.lower()
print(ex1)  # HELLO WORLD!
answer = input()
#  Type in Hello World!
if answer.lower() == 'hello world!':  # Will work when spam is input(), thus ignoring cases.
    print("Done correctly")

if answer.isupper():
    print("true")

print(','.join(['cat', ' bats', ' and rats ']))
print('\n\n'.join(['cat', 'bats', 'and rats']))

allSplit = 'My Name is Jonhahana'.split()

print(allSplit[-1])

print(allSplit[-1].rjust(20, '#'))

print(allSplit[-1].center(20, '#'))

string = 'AAAACCCCACCCCCCAAAAAA'.strip('A')  # Starts to strip char on either side of the string/ up until A stops


print(string)

print(sys.argv)