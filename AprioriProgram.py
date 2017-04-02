from imports.Apriori import Apriori
from imports.AprioriTid import AprioriTid
from imports.AprioriHybrid import AprioriHybrid
from imports.K1_Gen import K1_Gen
import csv

if __name__ == '__main__':
    print("...start program...")
    
    #input the data files name
    filename = raw_input("Please input the data file name: ")
    df = None
    rf = None
    try:
        with open(filename, 'r+') as csvfile:
            df = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rf = open('Rules.txt', 'w+')
    except IOError:
        print("Error: File cannot be opened. Try again.")
        exit(0)

    #input mode that will be run and run it
    b = True
    while b:
        mode = input("Please select the Apriori mode 1-3 (1 - Apriori, 2 - AprioriTid, 3 - AprioriHybrid): ")
        
        #get minimum support
        minsup = -1.0
        while minsup > 1 && minsup < 0:
            minsup =  input("Please input the minimum support(0.0 - 1.0): ")
        
        #get minimum confidence
        minconf - -1.0
        while minconf > 1 && minconf < 0:
            minconf = input("Please input the minimum confidence(0.0 - 1.0): ")
        
        if mode == 1:
            b = False
            print("Apriori selected.")
            itemset1 = K1_Gen(minsup, minconf, df)
            Apriori(minsup, minconf, df, itemset1)
        elif mode == 2:
            b = False
            print("AprioriTid selected.")
            itemset1 = K1_Gen(minsup, minconf, df)
            AprioriTid(minsup, minconf, df, itemset1)
        elif mode == 3:
            b = False
            print("AprioriHybrid selected.")
            itemset1 = K1_Gen(minsup, minconf, df)
            AprioriHybrid(minsup, minconf, df, itemset1)
        else:
            print("Incorrect input. Please input a proper mode number.")
        
    df.close()
    rf.close()
        
