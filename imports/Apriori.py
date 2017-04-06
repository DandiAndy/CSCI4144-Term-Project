from __future__ import division
from Apriori_Gen import Apriori_Gen

def Apriori(minsup, row_count, df, reader, k1):
    print("...begin apriori...")
    results = {}
    L = list(k1)
    while len(L) > 0:
        attributes = []
        Ck = Apriori_Gen(L)
        print(Ck)
        df.seek(0)
        supMap = {}
        i = 0
        for r in reader:
            tup = []
            #print(r)
            row = r[0].split(";")
            if i == 0:
                attributes = row
                i += 1
                continue
            else:
                j = 0
                for x in row:
                    tup.append("{}={}".format(attributes[j], x))
                    j += 1
            for c in Ck:
                #print("Tuple: {}".format(tup))
                #print("Current itemset: {}".format(c))
                if set(c).issubset(set(tup)):
                    #print("T: {} C: {}".format(tup, c))
                    key = ' '.join(str(e) for e in c)
                    #print(key)
                    if supMap.has_key(key):
                        supMap.update({key:supMap.get(key)+1})
                    else:
                        supMap.update({key:1})
                        
            #Remove based on support and recreate list from keys
            L = []
            for key in supMap.keys():
                if supMap.get(key)/row_count >= minsup:
                    l = key.split(" ")
                    print("Support: {} Key: {}".format(supMap.get(key)/row_count, l))
                    results.update({key:supMap.get(key)})
                    L.append(l)
    return results
