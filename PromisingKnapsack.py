maxprofit = 0
m = 10
w = [2, 3, 5]
p = [5, 8, 10]
n = len(w)
x = [0] * n  # آرایه انتخاب آیتم‌ها


def knapsack(i, profit, weight):
    global maxprofit

    if weight <= m and profit > maxprofit:
        maxprofit = profit
        print(f"جواب بهتر یافت شد: سود={profit}, انتخاب={x}")

    if promising(i, profit, weight):
        x[i] = 1
        knapsack(i + 1, profit + p[i], weight + w[i])

        x[i] = 0
        knapsack(i + 1, profit, weight)


def promising(i, profit, weight):
    if weight >= m:
        return False

    j = i + 1
    total_weight = weight
    bound = profit

    while j < n and total_weight + w[j] <= m:
        total_weight += w[j]
        bound += p[j]
        j += 1

    if j < n:
        bound += (m - total_weight) * (p[j] / w[j])

    return bound > maxprofit


print("=== شروع اجرا ===")
knapsack(0, 0, 0)
print(f"\nجواب نهایی: maxprofit = {maxprofit}")