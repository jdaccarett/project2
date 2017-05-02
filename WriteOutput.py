#import 1st algorithm
from algo1 import changeslowHelper as getChange1

#import 2nd algorithm
from algo2 import changegreedy as getChange2

#import 3rd algorithm
from algo3 import changeDP as getChange3

def main():

    with open("Amount.txt", "r") as f:
        with open('Amountchange.txt', 'w') as outputFile:
            count = -1
            testArray = []
            testNum = 0
            for line in f:
                count += 1
                # add each number from a line to an array
                if count % 2 == 0:
                    testArray = []
                    for i in line.split():
                        testArray.append(int(i))
                # take the amount number
                else:
                    for i in line.split():
                        testNum = int(i)
                    for algoID in xrange(1, 4):
                    # Write the name of the algorithm and store appropriate getChange function in variable
                        if(algoID == 1):
                            algoName = "Change Slow"
                            getChange = getChange1
                        elif(algoID == 2):
                            algoName = "Change Greedy"
                            getChange = getChange2
                        else:
                            algoName = "Change DP"
                            getChange = getChange3

                        outputFile.write('Running Algorithm: %s \n' %algoName)

                       # write each element of the array
                        outputFile.write('Input:[')
                        for i in xrange(0, len(testArray)):
                            #get rid of extra space when it is last element
                            if i != len(testArray) - 1:
                                outputFile.write('%d ' %testArray[i])
                            else:
                                outputFile.write('%d' %testArray[i])
                        outputFile.write(']\n')
            
                        # calculate the coin count and coin array
                        coinArray, coinCount = getChange(testArray, testNum)

                        # write the coin array          
                        outputFile.write('Coin Array: [')

                        for i in xrange(0, len(coinArray)):
                             #get rid of extra space when it is last element
                            if i != len(coinArray) - 1:
                                outputFile.write('%d ' %coinArray[i])
                            else:
                                outputFile.write('%d' %coinArray[i])


                        outputFile.write(']\n')

                        # write the coin count
                        outputFile.write('Number of Coins: %d\n\n' %coinCount)
                        

if __name__ == "__main__":
    main()