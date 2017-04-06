from __future__ import division

def K1_Gen(minsup, row_count, reader):
    print("...generate k-1 itemset...")
    #print(row_count)
    supMap = {}
    attributes = []
    i = 0
    for r in reader:
        row = r[0].split(";")
        if i == 0:
            attributes = row
            print(attributes)
            i += 1
        else:
            j = 0
            for x in row:
                key = "{}={}".format(attributes[j], x)
                if supMap.has_key(key):
                    supMap.update({key:supMap.get(key) + 1})
                else:
                    supMap.update({key:1})
                j += 1
    
                
    keys = supMap.keys()
    for k in keys:
        sup = supMap.get(k)/row_count
        if sup < minsup:
            supMap.pop(k, None)

    items = list(supMap.keys())
    items.sort()
    L1 = []
    for t in items:
        L1.append([t])
    #print("L1: {}".format(L1))
    return(L1)
    
