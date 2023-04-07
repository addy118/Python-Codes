a = input("Enter first number: ") 
# in the input function braces we need to write the text that is gonna show up before taking input
b = input("Enter second number: ")

c = int(input("Enter second number: "))
# directly TypeCasts the input as integer and then stores it in b

print("Addition of both gives", a+b)
# input function takes input as a string always so this operation will append the strings

print("Addition of both gives", int(a)+int(b))
# we need to convert the string input in required datatype by TypeCasting

print("Addition of both gives", int(a)+c)