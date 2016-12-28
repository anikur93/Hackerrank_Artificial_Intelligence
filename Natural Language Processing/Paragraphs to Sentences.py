import re
paragraph = str(input())

sentenceEnd = re.compile('!|\?|\.|\.\D|\.\s\|\^"|"$')
sentenceList = sentenceEnd.split(paragraph)
for i in range(50000):
    for j in range(50000):
        for sentence in sentenceList:
            print(sentence+str('.'))