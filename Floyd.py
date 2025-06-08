def Floyd(c,n):
    A = [[0] * n for _ in range(n)]
    path = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = c[i][j]

    for L in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][L] + A[L][j] < A[i][j]:
                    A[i][j] = A[i][L] + A[L][j]
                    path[i][j] = L

    return A , path

def printPath(i, j, path):
    if path[i][j] == -1:
        print(f"مستقیماً از {i} به {j} بروید")
        return
    x = path[i][j]
    printPath(i, x, path)  # مسیر از i به x
    print(f"از {x} عبور کنید")  # گره میانی
    printPath(x, j, path)  # مسیر از x به j

n = 4
INF = float('inf')
c = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]
A, path = Floyd(c, n)
print("کوتاه‌ترین مسیر از 0 به 3:")
print("0", end="")
printPath(0, 3, path)  # خروجی مثلاً: 0→1→2→3