import re
paragraph = str(input())
#Make words as in a list
sentenceEnd = re.compile(' |\.')
sentenceList = sentenceEnd.split(paragraph)
#for sentence in sentenceList:print(sentence)
#print(sentenceList)
sentencelist = [x for x in sentenceList if x != '']
#print(sentencelist)
#make trigrams with these words in list
trigrams = []
for i in range(len(sentencelist)-2):
    gram = (sentencelist[i], sentencelist[i+1], sentencelist[i+2])
    trigrams.append(gram)
#print(trigrams)
#finding most common trigram
word_counter = {}
for trigram in trigrams:
    if trigram in word_counter:
        word_counter[trigram] += 1
    else:
        word_counter[trigram] = 1
popular_trigram = sorted(word_counter, key = word_counter.get, reverse = True)
#print(popular_trigram)
result = popular_trigram[:1]
final = ''
for i in range(3):
    if i==0:
        final = final + result[0][i]
    else:
        final = final + ' ' + result[0][i]
print(final)