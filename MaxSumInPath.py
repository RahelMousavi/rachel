import random
n = 5
A = [[[ random.randint(0,50) ,0] for  j in range(i+1)]  for i in range(n) ]
B = [
    [[7, 0]],
    [[8, 0], [2, 0]],
    [[1, 0], [4, 0], [6, 0]],
    [[0, 0], [5, 0], [8, 0], [3, 0]],
    [[4, 0], [17, 0], [12, 0], [2, 0], [10, 0]]
]
print(A)
def SumMax(A,n):

    for i in range(n-2,-1,-1):
        for j in range(len(A[i])):
            if A[i+1][j][0] > A[i+1][j+1][0]:
                A[i][j][0] += A[i+1][j][0]
                A[i][j][1] = 0
            else:
                A[i][j][0] += A[i+1][j+1][0]
                A[i][j][1] = 1

    directions = []
    path = []
    j = 0
    for i in range(n - 1):
        path.append(A[i][j][0])
        direction = A[i][j][1]
        directions.append("left" if direction == 0 else "right")
        j += direction
    p = len(path)
    for i in range(p):
        print(f"{path[i]} → move to {directions[i]}")
    print(f"max sum is: {path[0]}")

SumMax(A,n)
