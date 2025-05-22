def Numbering(M, visit, Num, n, u, current_number):
    visit[u] = 1
    Num[u] = current_number  # همه رأس‌های هم‌مؤلفه شماره یکسان می‌گیرند

    for i in range(n):
        if M[u][i] == 1 and not visit[i]:
            Numbering(M, visit, Num, n, i, current_number)


def find_components(M, n):
    visit = [0] * n
    Num = [0] * n
    current_component = 1

    for u in range(n):
        if not visit[u]:
            Numbering(M, visit, Num, n, u, current_component)
            current_component += 1

    return Num

M = [
    [0,1,1,0,0],
    [1,0,1,0,0],
    [1,1,0,0,0],
    [0,0,0,0,1],
    [0,0,0,1,0]
]
n = 5

print(find_components(M, n))