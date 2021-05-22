n = 5
for i in range(n):
    for j in range(n-i-1):
        print(' ', end=' ')
    for j in range(2*i+1):
        print(i+1, end=' ') if(j == 0 or j == 2*i) else print(0, end=' ')
    print('')
