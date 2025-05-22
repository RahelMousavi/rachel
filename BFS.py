class queue:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def add(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)

    def delq(self):
        if not self.IsEmpty():
            return self.items.pop(0)

    def IsEmpty(self):
        return len(self.items) == 0

def BFS(s,n,visit,M):
    q = queue(n)
    q.add(s)
    visit[s]=1
    while not q.IsEmpty():
        x = q.delq()
        print(x)
        for i in range(n):
            if M[x][i] ==1 and visit[i]==0:
                q.add(i)
                visit[i]=1



n = 4
visit = [0] * n
M = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

BFS(0, n, visit, M)