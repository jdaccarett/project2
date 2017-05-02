#Dynamic Programming - Coin Change Problem
#Andrew Kim - CS 325

def changeDP(v, A):
    numCoins = [0 if idx == 0 else float("inf") for idx in xrange(A + 1)]            #create array that holds number of coins for solution - set 0 equal to 0 and the rest = inf
    lastCoinAdded = [-1 for _ in xrange(A + 1)]                                      #create array that holds the last coin added - set values as -1
    C = [0 for _ in xrange(len(v))]                                                  #initiate array c (answer array) with 0

    for j in xrange(len(v)):                                                         #for every different coin value
        for i in xrange(1, A + 1):                                                   #for every value up to the answer value
            coin = v[j]                                                             
            if i >= v[j]:                                                           #if the value is greater than the coin value
                if numCoins[i] > 1 + numCoins[i - coin]:                            #if the number of coins is greater than 1 + the number of coins from previous value
                    numCoins[i] = 1 + numCoins[i - coin]                            #increase the number of coins for the solution
                    lastCoinAdded[i] = j                                            #update the last coin added
    
    value = A
    while (value > 0):                                                              #update array c (answer array) with the number of coins used
        C[lastCoinAdded[value]] = C[lastCoinAdded[value]] + 1                       #find the last coin added and increase the array c[coin]
        value = value - v[lastCoinAdded[value]]                                     #subtract the value of the last coin and do it again until value = 0

    return C, numCoins[A]
