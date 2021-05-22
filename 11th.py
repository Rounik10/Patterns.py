def ncr(n, r):
    return fact(n)/(fact(r)*fact(n-r))


def fact(n):
    return 1 if(n <= 1) else n*fact(n-1)


n = 4
for i in range(n):
    for j in range(n-i-1):
        print(' ', end=' ')
    for j in range(i+1):
        print(int(ncr(i+1, j+1)), end='   ')
    print('')
