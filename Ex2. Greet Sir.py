import time
localTime = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

# without int TypeCasting
if(localTime >= '21:00:00'): # we can't replace the zeroes with blank
    print('Good Night Guys')
elif(localTime >= '18:00:00'):
    print('Good Evening Guys')
elif(localTime >= '12:00:00'):
    print('Good Afternoon Guys')
else:
    print('Good Morning Guys')

# with int TypeCasting
if(hour >= 21 and hour <= 23):
    print('Good Night Guys')
elif(hour == 0):
    print('Good Night Guys')
elif(hour >= 18 and hour < 21):
    print('Good Evening Guys')
elif(hour >= 12 & hour < 18):
    print('Good Afternoon Guys')
else:
    print('Good Morning Guys')
# when you TypeCast as int, you don't need to put ' ' in conditions