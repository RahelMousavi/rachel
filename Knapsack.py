def knapsack(V,W,m,n):
    items = sorted([(V[i] , W[i]) for i in range(n)], key= lambda item : item[0]/item[1], reverse = True)
    rc = m
    x = [0] * n
    for i in range(len(items)):
        v,w = items[i]
        if w <= rc:
            x[i] = 1
            rc -= w
        else:
            elem = rc / w
            x[i] = elem
            break

    return x


# مثال اجرا:
p = [60, 100, 120]  # ارزش‌ها
w = [10, 20, 30]  # وزن‌ها
m = 50  # ظرفیت کوله‌پشتی
n = len(p)
result = knapsack(p, w, m, n)
print(result)  # خروجی: [1, 1, 0.666...]