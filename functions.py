def add():
    print('Addition:', a+b)
# function without parameters only runs when 
# var(func defn) = var(program)

def swap(a, b):
    print('Before swap:', a, '<-->', b)
    temp = b
    b = a
    a = temp
    print('After swap:', a, '<-->', b)

a = int(input('Enter a number for addition: '))
b = int(input('Enter another number for addition: '))

c = int(input('Enter first number: '))
d = int(input('Enter second number: '))

add() # the var should be same else error will be thrown
swap(c, d)