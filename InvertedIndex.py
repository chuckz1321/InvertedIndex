import os
import re
import pickle
from string import digits

path = "E:/courses/UnstructuredData/Assignment2/corpus"
indexPath = "E:/courses/UnstructuredData/Assignment2/index/index"

files = os.listdir(path)

stopwords = ["and", "but", "is", "the", "to"]

docCount = 0;

indexMap = {}

# generate inverted index map
for file in files:
    docCount += 1
    f = open(path + "/" + file, encoding="utf-8")
    iter_f = iter(f)
    strTemp = ""
    # get file string
    for line in iter_f:
        strTemp += line
    # remove punc
        strTemp = re.sub(r'[^\w\s]',' ',strTemp)

    # remove digits
    remove_digits = strTemp.maketrans('','',digits)
    strTemp = strTemp.translate(remove_digits).lower()

    strTemp = strTemp.split()


    wordCount = 0

    for s in strTemp:
        wordCount += 1
        if s not in stopwords:
            if s not in indexMap.keys():
                indexMap[s] = {}
            if file not in indexMap[s].keys():
                indexMap[s][file] = []
            indexMap[s][file].append(wordCount)

f = open(indexPath, 'wb')
pickle.dump(indexMap,f)
f.close()
print(indexMap)
# eow AND profile