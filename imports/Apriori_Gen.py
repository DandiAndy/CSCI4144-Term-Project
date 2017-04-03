import itertools

def Apriori_Gen(itemset):
    print("...generate itemsets...")
    C = []
    for items1 in itemset:
        for items2 in itemset:
            if items1 != items2:
                nc = list(set(items2) - set(items1))
                if len(items1) > 1:
                    for item in nc:                        
                        a = list(items1)
                        a.append(item)
                        a.sort()
                        if a not in C:
                            C.append(a)
                else:
                    a = items1 + nc
                    if a not in C:
                        C.append(items1 + nc)
    
    #print C
    for c in C:
        km1subsets = [list(val) for val in itertools.combinations(c, len(c)-1)]
        #print(km1subsets)
        for km1 in km1subsets:
            if km1 not in itemset:
                #print c
                if c in C:
                    C.remove(c)
    return C
