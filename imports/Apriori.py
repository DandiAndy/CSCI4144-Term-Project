from __future__ import division
from Apriori_Gen import Apriori_Gen
import psutil
import sys
import time

def Apriori(minsup, row_count, df, reader, k1, hybridized):
    print("...begin apriori...")
    results = dict(k1)
    Lns = list(k1.keys())
    Lns.sort()
    L = []
    for t in Lns:
        L.append([t])

    #print L
    while len(L) > 0:
        start = time.time()
        attributes = []
        Ck = Apriori_Gen(L)
        #print(Ck)
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
        end = time.time()
        print "Apriori pass(seconds): {}".format(end-start)
        #Remove based on support and recreate list from keys
        L = []
        for key in supMap.keys():
            if supMap.get(key)/row_count >= minsup:
                l = key.split(" ")
                print("Support: {} Key: {}".format(supMap.get(key)/row_count, l))
                results.update({key:supMap.get(key)})
                L.append(l)
        #find out if we are using the hybrid algorithm
        #if we are check the memory estimate for ~Ck. If it will fit in mem, switch
        if len(supMap) > 0:
            mem_est = (sum(supMap.values()) + row_count) * sys.getsizeof(max(supMap.keys(), key=len)) 
        else:
            mem_est = 0
        print "Estimate: {} Available: {}".format(mem_est, psutil.virtual_memory().available)
        #print supMap
        if hybridized and len(supMap) > 0 and mem_est < psutil.virtual_memory().available - 100000:
            #returns L and false if memory is sufficient
            return supMap, results,  False

    #returns results and true if completed.
    return L, results, True
