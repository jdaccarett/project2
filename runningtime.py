import random
import time
#import 1st algorithm
from algo1 import changeslowHelper as getchange1

#import Juans's 2nd algorithm
from algo2 import changegreedy as getchange2

#import 3rd algorithm
from algo3 import changeDP as getchange3




def main():

    #3. Suppose
    # V1 = [1, 2, 6, 12, 24, 48, 60],
    # V2 = [1, 5, 10, 25, 50] and
    # V3 = [1, 6, 13, 37, 150],
    # for each integer value of A in [1, 2, 3, …, 50]
    # determine the number of coins that changeslow.
    # changegreedy and changedp requires for each denomination set.
    V1 = [1, 2, 6, 12, 24, 48, 60]
    V2 = [1, 5, 10, 25, 50]
    V3 = [1, 6, 13, 37, 150]
    questhree_Testcase = []
    questhree_Testcase.append(V1)
    questhree_Testcase.append(V2)
    questhree_Testcase.append(V3)



    for x in xrange(1, 4):
        algoID = x

        if (algoID == 1):
            getchange = getchange3

        elif (algoID == 2):
            getchange = getchange2


        elif (algoID == 3):
            getchange = getchange1


        # Loop for each integer value of A in [1, 2, 3, …, 50] in test cases V1, V2 and V3
        for amount in xrange(1, 51):
            if algoID > 0:
                start = time.clock()
                getchange(questhree_Testcase[0], amount)
                elapsed_time = (time.clock() - start)
                print("Algoid:", algoID, 'Amount = :', amount, ' ', 'Time:', elapsed_time)

        for amount in xrange(1, 51):
            if algoID > 0:
                start = time.clock()
                getchange(questhree_Testcase[1], amount)
                elapsed_time = (time.clock() - start)
                print("Algoid:", algoID, 'Amount = :', amount, ' ', 'Time:', elapsed_time)

        for amount in xrange(1, 51):
            if algoID >= 0:
                start = time.clock()
                getchange(questhree_Testcase[2], amount)
                elapsed_time = (time.clock() - start)
                print("Algoid:", algoID, 'Amount = :', amount, ' ', 'Time:', elapsed_time)




if __name__ == "__main__":
    main()
