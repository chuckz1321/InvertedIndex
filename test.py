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


map1 = {'a':[1],'b':[1]}

map2 = {'a':[4,8], 'b': [3,10]}

print(myAnd(map2,map1))