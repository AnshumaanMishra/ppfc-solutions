from random import shuffle
from math import log

query = list(range(1, 11))
shuffle(query)
print(query)

tournament = []
td = {}
query_div = 1
for i in range(0, int(log(len(query))/log(2))):
    winners = []
    for j in range(0, len(query) - 1, 2):
        print(query[j], query[j + 1])
        if(query[j] in td.keys()):
            td[query[j]].append(query[j + 1])
            td[query[j + 1]].append(query[j])
        else:
            td[query[j]]=([query[j + 1]])
            td[query[j + 1]]=([query[j]])

        if(query[j] > query[j + 1]):
            winners.append(query[j])
        else:
            winners.append(query[j + 1])
    key = len(query)
    if(key % 2 != 0):
        winners.append(query[key - 1])
        if(query[key - 1] in td.keys()):
            td[query[key - 1]].append(query[key - 1])
        else:
            td[query[key - 1]] = (query[key - 1])
    query = winners
    print(td)
    print(query)


max = query[0]

searchlist = td[max]

secmax = 0
for i in searchlist:
    if(i > secmax):
        secmax = i

print(max, secmax)
