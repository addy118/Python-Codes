color = ('red', 'yellow', 'green', 'red', 'brown', 'orange')
monotone = ('white', 'black')
nation = ('india',)
# we need put comma if one element is there in tuple
# else it will take tuple as integer/string

'''
# list to tuple interchanging
colors = list(color)
bright = color
# we can copy tuples like this 
# as copy() method doesn't exist in tuples

colors.append('black')
print(colors)

color = tuple(colors)
print(color)
print(bright)

print(color.index('red', 1, 5))
# gives index of red which is in between 1:5

print(color.count('yellow'))

wholeColor = color + monotone
print(wholeColor)

if 'red' in color:
    print('It exists')
else:
    print('It doesn\'t exists')

'''

