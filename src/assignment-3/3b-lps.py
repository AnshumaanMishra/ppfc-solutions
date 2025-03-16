s1 = "kjfdsjncjnkdjjkcnkdnmnzcn"
s2 = "ashdklsdhcjkcmjkfhkasdflxccdslzhlihjk"
s3 = "aaaaaaaaaaa"
s4 = "aaaaaaaaaa"

s = s4
memo = [[0 for _ in range(len(s))] for _ in range(len(s))]
memo2 = [["" for _ in range(len(s))] for _ in range(len(s))]

def lps(s: str, i:int, j:int):
    if(memo[i][j] == 0):
        if(i == j):
            memo[i][j] = 1
        elif(i == j - 1):
            if(s[i: j + 1] == s[j: i - 1: -1]):
                memo[i][j] = 2
            else:
                memo[i][j] = 1

        else:
            if(s[i] == s[j]):
                memo[i][j] = 2 + lps(s, i + 1, j - 1)
            else:
                val1 = lps(s, i, j - 1)
                val2 = lps(s, i + 1, j)
                memo[i][j] = max(val1, val2)
    return memo[i][j]

def recosntruct(s, i, j):
    if(memo[i + 1][j - 1] == 0 and memo[i][j] == 1):
        return s[i]
    elif(memo[i + 1][j - 1] == 0 and memo[i][j] == 2):
        return 2 * s[i]
    else:
        if(memo[i + 1][j - 1] != memo[i][j]):
            return s[i] + recosntruct(s, i + 1, j - 1) + s[i]
        else:
            return recosntruct(s, i + 1, j - 1)

print(lps(s, 0, len(s) - 1))
print(recosntruct(s, 0, len(memo[0]) - 1))
