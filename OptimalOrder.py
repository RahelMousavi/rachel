def Optimal(m, n, d):
    # مقداردهی صحیح ماتریس B
    B = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # مقداردهی اولیه قطر اصلی
    for i in range(1, n + 1):
        m[i][i] = 0

    # محاسبه بهینه
    for L in range(2, n + 1):  # طول زنجیره از 2 شروع شود
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + d[i - 1] * d[k] * d[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    B[i][j] = k  # ذخیره نقطه تقسیم بهینه

    return m[1][n], B

# ابعاد ماتریس‌ها: A1=10x30, A2=30x5, A3=5x60
d = [10, 30, 5, 60]  # طول d باید n+1 باشد (برای n ماتریس)
n = 3

# مقداردهی ماتریس‌ها
m = [[0 for _ in range(n+1)] for _ in range(n+1)]

# اجرای تابع
min_cost, B = Optimal(m, n, d)

print("حداقل هزینه:", min_cost)  # باید 4500 چاپ شود
print("نقاط تقسیم:")
for row in B[1:n+1]:
    print(row[1:n+1])