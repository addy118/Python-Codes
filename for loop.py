name = 'aditya'
avengers = ['loki', 'ultron', 'thanos', 'kang']

for char in name:
    print(char)

for let in 'addy':
    print(let)

for villian in avengers:
    print(villian)
    for letter in villian:
        print(letter)

# for loop runs the block once then starts again from first line with
# anohter variable

for num in range(9): 
    # range(0, 9, 1) 
    # # (0, n-1, 1)
    print(num)

for nums in range(3, 9):
    print(nums)

for step in range(1, 31, 2): 
    # (start, end, step)
    print(step) 
    # prints odd 
    # (0, n-1, 2) prints even
    # (0, n-1, m) prints m's divisible number
# step means increment by that number and stores that
# default step is 1

for rev in range(10, 0, -1):
    print(rev)

for revs in reversed(range(1, 11)):
    print(revs)