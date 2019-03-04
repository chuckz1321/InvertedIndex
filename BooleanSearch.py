import pickle
import os
import sys


# weak OR (eow OR of)
def compute():
    index1 = indexStack.pop()
    index2 = indexStack.pop()
    operation = operationStack.pop()
    if operation == and_str:
        backIndex = myAnd(index1,index2)
    elif operation == or_str:
        backIndex = myOr(index1,index2)
    indexStack.append(backIndex)

def myAnd(rmap, lmap):
    finalMap = {}
    for ldoc in lmap:
        if ldoc in rmap.keys():
            lindex = lmap[ldoc]
            rindex = rmap[ldoc]
            finalMap[ldoc] = lindex + rindex
            finalMap[ldoc].sort()
    return finalMap

def myOr(map1, map2):
    for doc in map2:
        if doc in map1.keys():
            for item in map2[doc]:
                map1[doc].append(item)
        else:
            map1[doc] = map2[doc]
    return map1


def pushIndex(word):
    if word in indexMap.keys():
        indexStack.append(indexMap[word])
    else:
        indexStack.append({})

indexPath = os.getcwd() + '/' + sys.argv[1]

and_str = "AND"
or_str = "OR"
open_paren = "("
close_paren = ")"

f = open(indexPath, 'rb')
# store indexMap
indexMap = pickle.load(f)
f.close()

queryString = input("plz input: ")
while queryString != 'exit()':
    indexStack = []
    operationStack = []
    words = []
    queryString = queryString.split()

    for c in queryString:
        if c == or_str or c == and_str:
            operationStack.append(c)
        elif c.find(close_paren) >= 0 :
            pushIndex(c[0:len(c)-1])
            words.append(c[0:len(c)-1])
            compute()
        elif c.find(open_paren) >= 0 :
            pushIndex(c[1:len(c)])
            words.append(c[1:len(c)])
        else:
            pushIndex(c)
            words.append(c)

    # clear stack
    while(len(operationStack) > 0):
        compute()

    allIndex = indexStack[0]

    for doc in allIndex:
        print(doc + ': ')
        for word in words:
            lineStr = '\t' + word + ':{'
            for index in allIndex[doc]:
                if doc not in indexMap[word].keys():
                    break
                if index in indexMap[word][doc]:
                    lineStr = lineStr + str(index) + ','
            if lineStr[-1] == ',':
                lineStr = lineStr[:len(lineStr)-1]
            print(lineStr+ '}')

    print('---------------------------------')
    print('input query sentence or \'exit()\' to exit')
    queryString = input()
# (weak AND eow) OR (yow AND of)



