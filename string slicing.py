name = 'addy'
lengthName = len(name)

print(len(name))
print(lengthName)

print(name[1:3])
# all the characters of index [1,3) will be included
print(name[2:4])
print(name[2:3])
print(name[0:4])
print(name[0:-2])
# this can be written as name[0:len(name)-2] ie. 4-2= 2 --> 0:2
print(name[-3:-2])