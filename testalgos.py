# This file will test all four functions using the same test cases

#import 2nd algorithm

#import 3rd algorithm

# import Juans's 2nd algorithm
from algo2 import changegreedy as getchange2


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


    testCase = []
    testCase.append(testOne)
    testCase.append(testTwo)
    testCase.append(testThree)


    coinAmount = [15, 29, 31]


    for x in range(1, 2):
        algoID = x

        if (algoID == 1):
            getchange = getchange2

        elif (algoID == 2):
            print("algoID",algoID)
            getchange = getchange2

        else:
            print(algoID)

        # Loop through test cases
        for testinput in range(0, len(testCase)):
            cArray, m = getchange(testCase[testinput], coinAmount[testinput])
            print("Array", cArray)
            print("m", m)


        # Loop for each integer value of A in [1, 2, 3, …, 50] in test cases V1, V2 and V3
        for amount in range(1, 51):
            #Values of V1
            cArray, m = getchange(questhree_Testcase[0], amount)
            print("AMOUNT of ", amount, "|" "ARRAY = ", cArray)
            print("Number of Coins = ", m)
            # Values of V2
            cArray, m = getchange(questhree_Testcase[1], amount)
            print("AMOUNT of ", amount, "|" "ARRAY = ", cArray)
            print("Number of Coins = ", m)
            # Values of V3
            cArray, m = getchange(questhree_Testcase[2], amount)
            print("AMOUNT of ", amount, "|" "ARRAY = ", cArray)
            print("Number of Coins = ", m)



        # For each integer value of A in [2000, 2001, 2002, …, 2200]
        # determine the number of coins that
        # changegreedy and changedp requires for each denomination set
        for amount in range(2000, 2200):
            #Values of V1
            cArray, m = getchange(questhree_Testcase[0], amount)
            print("AMOUNT of ", amount, "|" "ARRAY = ", cArray)
            print("Number of Coins = ", m)
            # Values of V2
            cArray, m = getchange(questhree_Testcase[1], amount)
            print("AMOUNT of ", amount, "|" "ARRAY = ", cArray)
            print("Number of Coins = ", m)
            # Values of V3
            cArray, m = getchange(questhree_Testcase[2], amount)
            print("AMOUNT of ", amount, "|" "ARRAY = ", cArray)
            print("Number of Coins = ", m)


if __name__ == "__main__":
    main()
