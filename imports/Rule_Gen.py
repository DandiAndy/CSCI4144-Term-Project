from __future__ import division

def Rule_Gen(supMap, itemset1, n, minConf, row_count):
    #print("...rule generation...")
    
    if n-1 <= 0:
        return
    
    itemset = itemset1.split(" ")
    conf = 0.0

    #find all itemsets in supMap that are n-1
    keys = supMap.keys()
    values = supMap.values()
    listN = list(keys)
    temp = []
    for nM1 in listN:
        t = nM1.split(" ")
        if len(t) == n-1:
            temp.append(t)
    #print "n-1: {} n: {}".format(len(temp[0]), len(itemset))
    if len(temp) > 0:
        for nM1 in temp:
            if set(nM1).issubset(set(itemset)):
                right = list(itemset)
                left = list(itemset)
                for i in itemset:
                    if i in nM1:
                        right.remove(i)
            
                for i in right:
                    if i in left:
                        left.remove(i)
                #right = [i for i in right if i not in nM1 or right.remove(i)] 
                #left = [i for i in left if i not in right or left.remove(i)]
                nM1 = ' '.join(nM1)
                conf = supMap[itemset1]/supMap[nM1]
                if conf >= minConf:
                    with open('Rules.txt', 'a') as myfile:
                        myfile.write("\nRule: ( Support = {} , Confidence = {} )".format(supMap[itemset1]/row_count, conf))
                        myfile.write("\n{} ---> {}\n".format(left, right))
                    Rule_Gen(supMap, itemset1, n-1, minConf, row_count)
                
    
    
