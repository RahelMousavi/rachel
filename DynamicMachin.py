def DChange(coins, m):
    inventory = []
    for value, count in coins.items():
        inventory.extend([value] * count)

    n = len(inventory)

    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        coin = inventory[i - 1]
        for j in range(m + 1):
            if dp[i - 1][j] != -1:
                dp[i][j] = dp[i - 1][j]
            if j >= coin and dp[i - 1][j - coin] != -1:
                if dp[i][j] < dp[i - 1][j - coin] + 1:
                    dp[i][j] = dp[i - 1][j - coin] + 1

    if dp[n][m] == -1:
        return []

    res = []
    i, j = n, m
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            res.append(inventory[i - 1])
            j -= inventory[i - 1]
            i -= 1

    return res

inv = {5: 3, 10: 3, 20: 2, 50: 3, 100: 1}
print(DChange(inv, 15))
