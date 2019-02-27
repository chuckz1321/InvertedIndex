import pickle
import re

indexPath = "E:/courses/UnstructuredData/Assignment2/index/index"

and_str = "AND"
or_str = "OR"
open_paren = "("
close_paren = ")"

f = open(indexPath, 'rb')
# store indexMap
indexMap = pickle.load(f)
f.close()
indexStack = []
operationStack = []


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


# 2 is left
def myAnd(rmap, lmap):
    finalMap = {}
    for ldoc in lmap:
        if ldoc in rmap.keys():
            lindex = lmap[ldoc]
            rindex = rmap[ldoc]
            ll = 0
            rr = 0
            while (ll != len(lindex)) & (rr != len(rindex)):
                if lindex[ll] + 1 == rindex[rr]:
                    if ldoc not in finalMap.keys() :
                        finalMap[ldoc] = []
                    finalMap[ldoc].append(lindex[ll])
                    ll += 1
                    rr += 1
                elif (lindex[ll] + 1 > rindex[rr]):
                    rr += 1
                else :
                    ll += 1
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



queryString = input("plz input:")

queryString = queryString.split()
print(queryString)

for c in queryString:
    if c == or_str or c == and_str:
        operationStack.append(c)
    elif c.find(close_paren) >= 0 :
        pushIndex(c[0:len(c)-1])
        compute()
    elif c.find(open_paren) >= 0 :
        pushIndex(c[1:len(c)])
    else:
        pushIndex(c)

# clear stack
while(len(operationStack) > 0):
    compute()

print(indexStack[0])




