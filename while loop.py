i = 1 # variable initialization is necessary
while (i < 11):
    print(i)
    i = i + 1 # without condition it will become infinite loop
else: # when the while condition fails, else executes
    print('i is greater than 10 now.')
print('We exited from the loops') 
# after else the code outside is executed
# do while doesn't exist in python