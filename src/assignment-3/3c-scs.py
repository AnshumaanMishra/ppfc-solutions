s1 = "zkabcdenmx"
s2 = "flcdefgmno"
xl = len(s1)
yl = len(s2)
memo = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]

def fillMemo(x, y):
    if x == 0:
        memo[x - 1][y - 1] =  y
    elif y == 0:
        memo[x - 1][y - 1] =  x
    elif s1[x - 1] == s2[y - 1]:
        memo[x - 1][y - 1] =  1 + fillMemo(x - 1, y - 1)
    else:   
        memo[x - 1][y - 1] =  1 + min(fillMemo(x - 1, y), fillMemo(x, y - 1))
        # memo[x - 1][y - 1] =  1 + fillMemo(x - 1, y - 1)
    return memo[x - 1][y - 1]

def reconstruct(i, j):
    if(i == xl - 1 and j == yl - 1):
        return s1[i] + s2[j]
    elif(i == xl - 1):
        return s2[j] + reconstruct(i, j + 1)
    elif(j == yl - 1):
        return s1[i] + reconstruct(i + 1, j)
    else:
        a1 = memo[i + 1][j]
        b1 = memo[i][j + 1]
        c1 = memo[i + 1][j + 1]
        if(a1 == -1):
            a1 = float('inf')
        if(b1 == -1):
            b1 = float('inf')
        if(c1 == -1):
            c1 = float('inf')
        a = reconstruct(i + 1, j)
        b = reconstruct(i, j + 1)
        c = reconstruct(i + 1, j + 1)
        m = max(a1, b1, c1)
        if(m == c1):
            if(c1 - memo[i][j] == 2):
                return s1[i] + s2[j] + c
            else:
                return s1[i] + c

        elif(m == b1):
            return s2[j] + b
        else:
            return s2[j] + a


fillMemo(xl, yl)
print(*memo, sep="\n")
print(memo[-1][-1])
print(reconstruct(0, 0))
