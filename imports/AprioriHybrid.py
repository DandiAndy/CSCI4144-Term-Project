from __future__ import division
from Apriori_Gen import Apriori_Gen
from Apriori import Apriori
from AprioriTid import AprioriTid

def AprioriHybrid(minsup, row_count, df, reader, k1):
    print("...begin aprioriHybrid...")
    L, aprioriResults, complete = Apriori(minsup, row_count, df, reader, k1, True)
    if complete:
        #if apriori returned a dictionary, it returned the completed results without being able to fit the ~Ck in mem. Return L
        return L
    else:
        results = AprioriTid(minsup, row_count, df, reader, L, True)
        results.update(aprioriResults)
        return results
