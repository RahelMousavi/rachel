def DFS(s,n,M,visit):
    visit[s]=1
    print(s)
    for i in range(n):
        if M[s][i]==1 and visit[i]==0:
            DFS(i,n,M,visit)

M = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
n = 4
visit = [0] * n  
DFS(0, n, M, visit)
