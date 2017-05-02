# This file will test all four functions using the same test cases

#import 1st algorithm
from algo1 import changeslowHelper as getchange1

#import Juans's 2nd algorithm
from algo2 import changegreedy as getchange2

#import 3rd algorithm
from algo3 import changeDP as getchange3




def main():

    #Test Cases
    testOne = [1,2,4,8]
    testTwo = [1,3,7,12]
    testThree = [1,3,7,12]


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


    #testCase = []
    #testCase.append(testOne)
    #testCase.append(testTwo)
    #testCase.append(testThree)


    coinAmount = [15, 29, 31]


    for x in xrange(1, 4):
        algoID = x

        if (algoID == 1):
            getchange = getchange3

        elif (algoID == 2):
            getchange = getchange2


        elif (algoID == 3):
            getchange = getchange1

        # Loop through test cases
        #for x in xrange(0, len(testCase)):
         #   print("ALGO ID:", algoID)
          #  cArray, m = getchange(testCase[x], coinAmount[x])
           # print(cArray)
            #print(m)


        # Loop for each integer value of A in [1, 2, 3, …, 50] in (test case V1)
        print("ALGO ID:", algoID, "TESTCASE V1,V2,V3  A[1,2,3..50]")
        print("____________________________________________ ")
        for amount in xrange(1, 51):
            if algoID > 0:
                # Values of V1
                cArray, m = getchange(questhree_Testcase[0], amount)
                print(cArray)
                print("AlgoId",algoID, "Number of Coins = ", m)

        # Loop for each integer value of A in [1, 2, 3, …, 50] in (test case V2)
        print("ALGO ID:", algoID, "TESTCASE V1,V2,V3  A[1,2,3..50]")
        print("____________________________________________ ")
        for amount in xrange(1, 51):
            if algoID > 0:
                # Values of V2
                cArray, m = getchange(questhree_Testcase[1], amount)
                print(cArray)
                print("AlgoId",algoID, "Number of Coins = ", m)

        # Loop for each integer value of A in [1, 2, 3, …, 50] in (test case V3)
        print("ALGO ID:", algoID, "TESTCASE V1,V2,V3  A[1,2,3..50]")
        print("____________________________________________ ")
        for amount in xrange(1, 51):
            if algoID > 0:
                # Values of V2
                cArray, m = getchange(questhree_Testcase[2], amount)
                print(cArray)
                print("AlgoId",algoID, "Number of Coins = ", m)



        # For each integer value of A in [2000, 2001, 2002, …, 2200]
        print("ALGO ID:", algoID, "TESTCASE V1,V2,V3  A[2000,2001,2002,…2200]")
        print("____________________________________________")
        #V1 case
        for amount in xrange(2000, 2200):
            #Values of V1
            cArray, m = getchange(questhree_Testcase[0], amount)
            print(cArray)
            print("AlgoId", algoID, "Number of Coins = ", m)

        print("ALGO ID:", algoID, "TESTCASE V1,V2,V3  A[2000,2001,2002,…2200]")
        print("____________________________________________")
        #V2 case
        for amount in xrange(2000, 2200):
            # Values of V2
            cArray, m = getchange(questhree_Testcase[1], amount)
            print(cArray)
            print("AlgoId", algoID, "Number of Coins = ", m)

        print("ALGO ID:", algoID, "TESTCASE V1,V2,V3  A[2000,2001,2002,…2200]")
        print("____________________________________________")
        #V3 Case
        for amount in xrange(2000, 2200):
            # Values of V3
            cArray, m = getchange(questhree_Testcase[2], amount)
            print(cArray)
            print("AlgoId", algoID, "Number of Coins = ", m)


if __name__ == "__main__":
    main()
