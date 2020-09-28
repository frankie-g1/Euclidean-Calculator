cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

allCats = []

allCats.append(cat)
allCats.append({'size': 'fat', 'color': 'gray', 'disposition': 'loud'})
allCats.append(1)

print(allCats)

# Lists can really hold any data type
# Organized ones are better for programs to interpret

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ',
            'low-M': ' ', 'low-R': ' '}

import pprint

theBoard['mid-M'] = 'X'
theBoard['mid-L'] = 'X'
theBoard['mid-R'] = 'X'
theBoard['top-L'] = 'O'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'
theBoard['low-L'] = 'X'
theBoard['low-M'] = 'X'
theBoard['low-R'] = 'X'

pprint.pprint(theBoard)


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + '|')
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] + '|')
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + '|')
    print('-----')


printBoard(theBoard)

print(type(42))
print(type(allCats))
print(type(theBoard))
print(type(theBoard['top-L']))  # Says 'X' string is the value.