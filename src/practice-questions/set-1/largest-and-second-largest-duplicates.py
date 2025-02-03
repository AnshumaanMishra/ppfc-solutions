# from random import shuffle
from math import log
from random import randrange

query = [randrange(1, 11) for _ in range(10)]
# query = [2] * 9
print(query)

tournament = []
td = {}
query_div = 1
for i in range(0, int(log(len(query))/log(2)) + 1):
    winners = []
    for j in range(0, len(query) - 1, 2):
        if(query[j + 1] != query[j]):
            if(query[j] in td.keys()):
                td[query[j]].append(query[j + 1])
            else:
                td[query[j]] = [query[j + 1]]
            if(query[j + 1] in td.keys()):
                td[query[j + 1]].append(query[j])
            else:
                td[query[j + 1]] = [query[j]]

        if(query[j] > query[j + 1]):
            winners.append(query[j])
        else:
            winners.append(query[j + 1])
    key = len(query)
    if(key % 2 != 0):
        winners.append(query[key - 1])
        if(query[key - 1] not in td.keys()):
            td[query[key - 1]] = ([query[key - 1]])
    query = winners
    # print(td)
    # print(query)


max = query[0]

searchlist = td[max]

secmax = 0
for i in searchlist:
    if(i > secmax):
        secmax = i
print(f"Max = {max}, SecMax = {secmax}")
