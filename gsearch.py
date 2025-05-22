def BFS(s, n, visit, M):
    q = []
    q.append(s)
    visit[s] = 1

    while q:
        x = q.pop(0)
        print(x, end=" ")

        for i in range(n):
            if M[x][i] == 1 and visit[i] == 0:
                q.append(i)
                visit[i] = 1
                
def gsearch(M, n, visit):
    for i in range(n):
        if visit[i] == 0:
            print(f"\nمؤلفه همبند جدید از رأس {i}:")
            BFS(i, n, visit, M)

M = [
    [0,1,1,0,0],
    [1,0,1,0,0],
    [1,1,0,0,0],
    [0,0,0,0,1],
    [0,0,0,1,0]
]
n = 5
visit = [0]*5
gsearch(M, n, visit)