num = int(input('Enter a number: '))

match num:
    case 1:
        print('One')
    case 2:
        print('Two')
    case 3:
        print('Three')
    case 4 if num == 4:
        print('Four')
    case _ if num == 5:
        print('Five')
    case _:
        print('Big Number')
# the blank default always comes in last
# no break statement is needed in python