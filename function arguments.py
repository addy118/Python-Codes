def avg(b, c, d=2):
    # here, 
    # c is the default argument
    # a, b, c are the required arguments
    # after default arg, non-default arg cannot be written
    print('The average is', (a+b+c+d)/2)

a = int(input('Enter a number: '))
# a is directly used in the formula defined in print

avg(c=2, b=2)
# here, key=value
# b and d are keyword argument
# the order of b and d doesn't matter
# any one can written before the other

# variable-length arguments
# 1. arbitrary (tuple)
#    initialize by *tuple_name
# 2. keyword arbitrary (dict)
#    initialize by **dict_name

def name(*name):
    # for arbitrary arg
    print('Hello,', name[0], name[1], name[2]) # prints 3 elements of tuple
name('Aditya', 'Narendra', 'Kirti') # name func is called with 3 arg
# tupleElements < callArguments

def trio(**trio):
    # for keyword arbitrary
    print('Hello,', trio['name1'], ',', trio['name2'], '&', trio['name3'])
trio(name1 = 'Harry', name2 = 'Ron', name3 = 'Hermione') # trio func is called