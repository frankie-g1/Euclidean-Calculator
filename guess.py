import random
print('Hello. What is your name?')
name = input()
r = random.randint(1, 20)
# A comma adds space and plus doesn't.
print("Well,", name + ", I am thinking of a number between 1 and 20")
print('Take a guess')
for x in range (6):
    number = int(input())
    if (number < r):
        print('Too low!')
    elif (number > r):
        print('Too high!')
    else:
        break

if(number == r):
    print('Correct! It took you ' + str(x) + ' tries.')
else:
    print('Sorry, it was ' + str(r))

