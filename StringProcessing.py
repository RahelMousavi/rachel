def I(char):
    return 1.5

def D(char):
    return 1.2

def Ex(char1, char2):
    return 2 if char1 != char2 else 0

def StringProcessing(x,y, D, I, Ex):
    n, m = len(x), len(y)
    c = [[0] * (m + 1) for _ in range(n + 1)]

    c[0][0] = 0
    for i in range(1, n + 1):
        c[i][0] = c[i - 1][0] + D(x[i - 1])
    for j in range(1, m + 1):
        c[0][j] = c[0][j - 1] + I(y[j - 1])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                substitution_cost = c[i - 1][j - 1]
            else:
                substitution_cost = c[i - 1][j - 1] + Ex(x[i - 1], y[j - 1])  # هزینه تغییر
            c[i][j] = min(
                c[i][j - 1] + I(y[j - 1]),
                c[i - 1][j] + D(x[i - 1]),
                substitution_cost
            )
    return c[n][m]

x = "aabab"
y = "babb"
cost = StringProcessing(x, y, D, I, Ex)
print(cost)