print('Hello world')
print("What is your name?")
name = input()
print('it is nice to meet you ' + name)
print("the length of your name is", len(name))
print("what is your age?")
age = input()
print("your age is " + age)
print("you will be ",  (int(age) + 1), " in a year")
#print('you will be ' + str(int(age) + 1) + ' in a year')
#cannot concatenate with ints, therefore line 9 only works with large quotations
