from random import randrange

n = 5
m = 10
query = []
for _ in range(n):
    query.append(sorted([randrange(1, n * m + 1) for _ in range(m)]))

indices = [0] * n

pq = [query[i][indices[i]] for i in range(n)]

def merge(arr1, arr2):
    lp = 0
    rp = 0
    merged = []
    for _ in range(len(arr1) + len(arr2)):
        print(lp, rp)
        if(lp >= len(arr1)):
            merged.append(arr2[rp])
            rp += 1
            continue
        if(rp >= len(arr2)):
            merged.append(arr1[lp])
            lp += 1
            continue
        if(arr1[lp] > arr2[rp]):
            merged.append(arr2[rp])
            rp += 1
        else:
            merged.append(arr1[lp])
            lp += 1
    return merged

print(merge(query[0], query[1]))
# while

sum = 0
max = query[0][0]
maxi = 0
mini = 0
min = query[0][0]
while(sum < m * n):
    for i, element in enumerate(pq):
        current = query[i][element]
        if(current > max):
            max = current
            maxi = i
    sum += 1

print(query)