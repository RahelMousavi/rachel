inv = {5: 5, 10: 3, 20: 2, 50: 3, 100: 1}


def exmachin(m, inv):
    k = sorted(inv.keys(), reverse=True)  # باید از بزرگ به کوچک باشد
    v = [inv[j] for j in k]
    result = []

    def coin(cm, k, v, i):
        if i >= len(k):  # شرط توقف وقتی به آخر لیست رسیدیم
            return

        if k[i] <= cm and v[i] > 0:  # اگر سکه قابل استفاده است
            cm -= k[i]
            v[i] -= 1
            result.append(k[i])
            coin(cm, k, v, i)  # همان سکه را دوباره بررسی کن
        else:
            coin(cm, k, v, i + 1)  # به سکه بعدی برو

    coin(m, k, v, 0)
    return result if m == sum(result) else []



print(exmachin(200,inv))