for i in range(1, 16):
    if(i==13):
        print('Loop exited!')
        break
    # at 6*13 loop will be exited without printing coz break is before print
    if(i==10):
        print('Iteration skipped due to easiness!')
        # iteration i=10 is skipped
        continue
    # at 6*10, this particular case will be skipped and 6*11 will be printed
    print('6 x', i, '=', 6*i)