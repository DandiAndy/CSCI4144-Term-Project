def Rule_Gen(supMap, itemset1, n, minConf):
    print("...rule generation...")

    if n-1 < 0:
        return
    
    itemset = itemset1.split(" ")
    right = list(itemset)
    left = list(itemset)

    conf = 0.0

    #find all itemsets in supMap that are n-1
    keys = supMap.keys()
    values = supMap.values()
    listN = list(keys.split(" "))
    temp = []
    for nM1 in listN:
        if len(nM1) > n-1:
            temp.append(nM1)

    itemset = list(itemset.split(" "))
    for nM1 in temp:
        if nM1 in itemset:
            right[:] = [item for item in right if item != nM1]
            left[:] = [item for item in left if item != right]
            conf = supMap[itemset]/supMap[nM1]

            if conf >= (minConf/100):
                print("\nRule: (Support = " + supMap[itemset] + ", Confidence = " + conf + ")")
                print("\n"+left[0:len(left)]+" ----> "+right[0:len(right)])
                Rule_Gen(supMap, itemset, n-1, minConf)
                
            right = list(itemset)
            left = list(itemset)
    
    
