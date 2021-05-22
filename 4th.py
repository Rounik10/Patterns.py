n = 5
for i in range(2*n-1):
    if(i < (2*n-1)//2):
        for j in range(n-1-i):
            print(' ', end=' ')
        for j in range(i+1):
            print('*', end=' ')
    else:
        for j in range(i-(2*n-1)//2):
            print(' ', end=' ')
        for j in range(n-i+(2*n-1)//2):
            print('*', end=' ')
    print('')
