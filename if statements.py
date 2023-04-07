num = int(input('Enter a number: \n'))

if(num < 0):
    if(num < -10):
        print("Number lies in (-10,-infinity)")
    else:
        print("Number lies in [-10, 0)")

elif(num == 0):
    print("Number is zero")
    
else:
    if(num > 10):
        print("Number lies in (10, infinity)")
    else:
        print("Number lies in (0,10]")
