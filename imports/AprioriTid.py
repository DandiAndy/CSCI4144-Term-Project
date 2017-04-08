from __future__ import division
from Apriori_Gen import Apriori_Gen
import itertools

def AprioriTid(minsup, row_count, df, reader, k1):
    print("...begin aprioriTid...")
    
    #generate Ct from the database. Ct is the db stored in mem.
    Cm = {}
    attributes = []
    i = 0
    df.seek(0)
    for r in reader:
        tup = []
        row = r[0].split(";")
        if i == 0:
            attributes = row
            i += 1
            continue
        else:
            j = 0
            for x in row:
                item = "{}={}".format(attributes[j], x)
                tup.append([item])
                j += 1
            Cm.update({i:tup})
            i += 1
    
    #print(Cm)
    
    #start AprioriTid
    results = {} 
    L = list(k1)
    while len(L) > 0:
        Ck = Apriori_Gen(L)
        supMap = {}
        temp_Cm = {}
        for c in Ck:
            Cm_keys = Cm.keys()
            for k in Cm_keys:
                superset = list(set(itertools.chain.from_iterable(Cm.get(k))))
                print("Superset: {} C: {}".format(superset, c))
                if set(c).issubset(set(superset)):
                    key = ' '.join(str(e) for e in c)
                    if supMap.has_key(key):
                        supMap.update({key:supMap.get(key) + 1})
                        if temp_Cm.has_key(k):
                            lv = list(temp_Cm.get(k)) + [c]
                            temp_Cm.update({k:lv})
                        else:
                            temp_Cm.update({k:[c]})

                    else:
                        supMap.update({key:1})
                        if temp_Cm.has_key(k):
                            lv = list(temp_Cm.get(k)) + [c]
                            temp_Cm.update({k:lv})
                        else:
                            temp_Cm.update({k:[c]})


        #print temp_Cm
        L = []
        Cm = dict(temp_Cm)
        temp_Cm = {}
        for key in supMap.keys():
            if supMap.get(key)/row_count >= minsup:
                    l = key.split(" ")
                    print("Support: {} Key: {}".format(supMap.get(key)/row_count, l))
                    results.update({key:supMap.get(key)})
                    L.append(l)
    return results
