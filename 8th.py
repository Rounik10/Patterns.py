n = 10
for i in range(n):
    for j in range(n+i+1):
        if(j >= n-i):
            num = j if(j < n) else (n-j) % 10
            print(num, end=' ')
        else:
            print(' ', end=' ')
    print('')
