l = [1, 5, 18, 9, 3, 9, 8]
m = [84, 28, 34, 42, 12]

'''
# list_name.sort()
l.sort()
print(l)

# list_name.reverse()
l.reverse()
print(l)

# list_name.append()
l.append(92) # only one arg can be given else error
print(l)

# list_name.pop() # deletes the element of given index
l.pop(2) # deletes 18
print(l)

# list_name.extend(another_list)
l.extend(m)
print(l)

# list_name.copy()
# if we do 
n = l
# n acts as a reference, if you change n, l will be changed
n[0] = 4
print(n)
k = l.copy()
# here, k will be a copy of l and not reference
print(l, k, sep='\n')

# list_name.index(element)
print(l.index(8))

# list_name.count(element)
print(l.count(9))

# list_name.insert()
l.insert(2, 28) # inserts 28 at index 2
print(l)
'''

