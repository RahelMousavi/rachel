def is_safe(k, i, x):
    for j in range(1, k):
        if x[j] == i or abs(j - k) == abs(x[j] - i):
            return False
    return True

def btqueens(k, n, x):
    for i in range(1, n + 1):
        if is_safe(k, i, x):
            x[k] = i
            if k == n:
                print(x[1:n + 1])
            else:
                btqueens(k + 1, n, x)


n = 4
x = [0] * (n + 1)
btqueens(1, n, x)