def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error you tried to divide by zero.')

print(div42by(2))
print(div42by(0)) #prints None value
print(div42by(12))

def cats():
    #errors that happen inside a try block will be caught be except block
    #code in try block is ran before code outside try block
    try:
        print("how many cats do you have?")
        numCats = input()
        if int(numCats) >= 4:
            print("Das alot of cats")
        elif int(numCats) < 0:
            print('Wow')
        else:
            print("Not alot of cats")
    except ValueError:
        print('You did not enter a number')

cats()