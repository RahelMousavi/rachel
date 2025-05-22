def topo_sort(M, visit, n, u, result):
    visit[u] = 1  # Mark as visiting

    for v in range(n):
        if M[u][v]==1:
            if visit[v] == 1:
                raise ValueError("Cycle detected!")
            if visit[v] == 0:
                topo_sort(M, visit, n, v, result)

    visit[u] = 2  # Mark as done
    result.append(u)
    return result[::-1]

# ماتریس مجاورت
M = [
    [0,1,1,0],
    [0,0,0,1],
    [0,1,0,0],
    [0,0,0,0]
]
n = 4
visit = [0] * n
result = []
# شروع از رأس 0
sorted_order = topo_sort(M, visit, n, 0,result)
print(sorted_order)  # خروجی ممکن: [2, 0, 1, 3]