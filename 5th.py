n = 7
for i in range(n):
    for j in range(n):
        if(i <= n//2):
            if(j <= n//2):
                print('*', end=' ') if(i+j < n//2) else print(' ', end=' ')
            else:
                print('*', end=' ') if(i < j-n//2) else print(' ', end=' ')
        else:
            if(j < n//2):
                print('*', end=' ') if(i-n//2 > j) else print(' ', end=' ')
            else:
                print('*', end=' ') if(i+j >= n+n//2) else print(' ', end=' ')
    print('')
