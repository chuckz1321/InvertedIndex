import sys
import os
import pickle

indexMap = {}
indexPath = os.getcwd() + '/' + sys.argv[1]

for line in sys.stdin:
    aItem = eval(line)
    indexMap.update(aItem)

f = open(indexPath, 'wb')
pickle.dump(indexMap,f)
f.close()
print(indexMap)