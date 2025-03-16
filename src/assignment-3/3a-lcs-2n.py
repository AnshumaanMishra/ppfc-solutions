s1 = "abcdefgabcde"
s2 = "efgacfd"
s3 = ""
xl = len(s1)
yl = len(s2)
if(xl < yl):
    xl, yl = yl, xl
    s1, s2 = s2, s1

prev = [0 for _ in range(yl)]
curr = [0 for _ in range(yl)]

def fillMemo(prev, curr):
    for i in range(xl):
        for j in range(yl):
            decision = int(s1[i] == s2[j])
            if(i == 0):
                if(j == 0):
                    curr[j] = decision
                else:
                    curr[j] = curr[j - 1] + decision
            else:
                if(j != 0 and s1[i] == s2[j]):
                    curr[j] = prev[j - 1] + decision
                elif(j == 0):
                    curr[j] = prev[j] + decision
                else:
                    t1 = curr[j - 1] + decision
                    t2 = prev[j] + decision
                    curr[j] = max(t1, t2)
        prev = curr.copy()

    return prev, curr, curr[-1]
    

prev, curr, answer = fillMemo(prev, curr)
print(f"{prev}, {curr}, {answer}")