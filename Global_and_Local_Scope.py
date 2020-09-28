
def eggs():
    spam = 42 # local variable
    print(spam)

#eggs()
#assignment statement inside the def eggs is prioritized over global variable

spam = 41 #global variable

def bacon():
    global spam
    spam = 58
    print(spam)

#Global, local, then use global in def.
print(spam) 
eggs()
bacon()
