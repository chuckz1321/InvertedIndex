import os
import re
import pickle
import sys



# corpus folder name
corpusPath = os.getcwd() + '/' + sys.argv[1]
# output file name
indexPath = os.getcwd() + '/' + sys.argv[2]

files = os.listdir(corpusPath)

stopwords = ["and", "but", "is", "the", "to"]

indexMap = {}
indexList = []

# generate inverted index map
for file in files:
    f = open(corpusPath + "/" + file, encoding="utf-8")
    iter_f = iter(f)
    strTemp = ""
    # get file string
    for line in iter_f:
        strTemp += line

    #print(strTemp)

    # remove digits
    # remove_digits = strTemp.maketrans('','',digits)
    # strTemp = strTemp.translate(remove_digits).lower()

    strTemp = strTemp.lower()

    #remove punc
    strTemp = re.sub(r'[^\w\s]',' ',strTemp)
    strTemp = strTemp.split()


    wordCount = 0

    for s in strTemp:
        wordCount += 1
        if (not bool(re.search('[a-z]', s))) | (s in stopwords): continue
        if s not in indexMap.keys():
            indexMap[s] = {}
        if file not in indexMap[s].keys():
            indexMap[s][file] = []
        indexMap[s][file].append(wordCount)

f = open(indexPath, 'wb')
pickle.dump(indexMap,f)
f.close()