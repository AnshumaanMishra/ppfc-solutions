from random import shuffle

query = list(range(1, 11))
shuffle(query)
print(query)

winners = []
losers = []

comparisons = 0

for i in range(0, len(query) - 1, 2):
    comparisons += 1
    if(query[i] > query[i + 1]):
        winners.append(query[i])
        losers.append(query[i + 1])
    else:
        winners.append(query[i + 1])
        losers.append(query[i])

print(f"Comparisons involved in division of groups = {comparisons}")
comparisons = 0

if(len(query) % 2 == 1):
    winners.append(query[-1])

min = losers[0]
max = winners[0]

for i in range(1, len(winners)):
    comparisons += 1
    if(winners[i] > max):
        max = winners[i]

print(f"Comparisons involved in finding Max = {comparisons}")
comparisons = 0

for i in range(1, len(losers)):
    comparisons += 1
    if(losers[i] < min):
        min = losers[i]

print(f"Comparisons involved in finding Min = {comparisons}")
print(f"Max = {max}, Min = {min}")