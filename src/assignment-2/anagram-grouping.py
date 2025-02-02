inputList = ["eat", "tea", "tan", "ate", "nat", "bat"]
# For Manual Input:
# inputList = input("Enter the words, space separated").split(' ')
frequencyDict = {}

for i in inputList:
    currentKey = ''.join(sorted(i))
    if(currentKey in list(frequencyDict.keys())):
        frequencyDict[currentKey].append(i)
    else:
        frequencyDict[currentKey] = [i]

answerList = [value for value in frequencyDict.values()]

print(answerList)
