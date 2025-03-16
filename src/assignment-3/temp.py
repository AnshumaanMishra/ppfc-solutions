n, W = input().split(" ")
n, W = int(n), int(W)

weights = list(map(int, input().split(" ")))
values = list(map(int, input().split(" ")))
memoBU = [[-1 for _ in range(n)] for _ in range(W)]
def bottomUp(i, j):
    if(i < 0 or j < 0):
        return 0
    newj = j - 1
    newi = i - weights[j]
    if(weights[j] > i + 1):
        memoBU[i][j] = bottomUp(i, newj)
    else:
        memoBU[i][j] = max(values[j] + bottomUp(newi, newj), bottomUp(i, newj))
    return memoBU[i][j]

print(bottomUp(W - 1, n - 1))

