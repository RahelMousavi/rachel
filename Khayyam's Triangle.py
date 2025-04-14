def comb(n, k):
    c = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        c[i][0] = 1

    for j in range(1, k + 1):
        c[j][j] = 1

    for i in range(2, n + 1):
        for j in range(1, min(i, k + 1)):
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j]

    return c

def print_matrix(matrix):
    for row in matrix:
        print(row)

n, k = 6 ,4
result_matrix = comb(n, k)
print_matrix(result_matrix)
print(f"\nC({n},{k}) = {result_matrix[n][k]}")