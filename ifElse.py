name = 'f'
if name == 'Alice':
    print('hello alice')
else:
    print('fuck')
print('done')

password = 'swordfish'
if password == 'swordfish':
    print('Accessed')
else:
    print('Denied')

spam = '0'
while int(spam) < 80:
    print(spam)
    spam = int(spam) + 1


for i in range(89):
    print("oof")

total = 0
#does not execute once n is 100
for n in range(100):
    total = total + n
print(total)

#range data type

range(10)

for i in range(12, 18):
    print("Jimmy 6 times ", int(i-11))
print()
#goes backwards
for i in range(18, 12, -1):
    print("Jimmy 6 times ", int(i-12))
