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

        # Loop through each test case
        for testinput in range(0, len(testCase)):
            cArray, m = getchange(testCase[testinput], coinAmount[testinput])
            print("Array", cArray)
            print("m", m)


if __name__ == "__main__":
    main()
