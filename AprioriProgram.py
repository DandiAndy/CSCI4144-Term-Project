from imports.Apriori import Apriori
from imports.AprioriTid import AprioriTid
from imports.AprioriHybrid import AprioriHybrid
from imports.K1_Gen import K1_Gen
from imports.Rule_Gen import Rule_Gen
import csv
import time

if __name__ == '__main__':
    print("...start program...")
    
    #input the data files name
    filename = raw_input("Please input the data file name: ")
    df = None
    rf = None
    row_count = 0
    try:
        df = open(filename, 'r+')
        reader = csv.reader(df, delimiter=' ', quotechar='|')
        row_count = len(list(reader)) - 1
        df.seek(0)
        rf = open('Rules.txt', 'w+')
    except IOError:
        print("Error: File cannot be opened. Try again.")
        exit(0)
        
    print(row_count)
    #input mode that will be run and run it
    b = True
    while b:
        mode = input("Please select the Apriori mode 1-3 (1 - Apriori, 2 - AprioriTid, 3 - AprioriHybrid): ")
        
        #get minimum support
        minsup = -1.0
        while minsup > 1 or minsup < 0:
            minsup =  input("Please input the minimum support(0.0 - 1.0): ")
        
        #get minimum confidence
        minconf = -1.0
        while minconf > 1 or minconf < 0:
            minconf = input("Please input the minimum confidence(0.0 - 1.0): ")
        
        with open('Rules.txt', 'a') as myfile:
            string = "Summary:\nTotal rows in the original set: {}\nThe selected measures: Support={} Confidence={}\n".format(row_count, minsup, minconf)
            myfile.write(string)
            myfile.write("-------------------------------------------------------------")
        if mode == 1:
            b = False
            print("Apriori selected.")
            itemset1 = K1_Gen(minsup, row_count, reader)
            start = time.time()
            L, results, complete = Apriori(minsup, row_count, df, reader, itemset1, False)
            end = time.time()
            print "Apriori elapsed time(seconds): {}".format(end - start)
            for cand_set in results.keys():
                c = list(cand_set.split(" "))
                Rule_Gen(results, cand_set, len(c), minconf, row_count)
        elif mode == 2:
            b = False
            print("AprioriTid selected.")
            itemset1 = K1_Gen(minsup, row_count, reader)
            start = time.time()
            results = AprioriTid(minsup, row_count, df, reader, itemset1, False)
            end = time.time()
            print "AprioriTid elapsed time(seconds): {}".format(end - start)
            for cand_set in results.keys():
                c = list(cand_set.split(" "))
                Rule_Gen(results, cand_set, len(c), minconf, row_count)
        elif mode == 3:
            b = False
            print("AprioriHybrid selected.")
            itemset1 = K1_Gen(minsup, row_count, reader)
            start = time.time()
            results = AprioriHybrid(minsup, row_count, df, reader, itemset1)
            end = time.time()
            print "Apriori Hybrid elapsed time(seconds): {}".format(end - start)
            for cand_set in results.keys():
                c = list(cand_set.split(" "))
                Rule_Gen(results, cand_set, len(c), minconf, row_count)
        else:
            print("Incorrect input. Please input a proper mode number.")
        
    df.close()
    rf.close()
        
