#Dynamic Programming - Coin Change Problem
#Andrew Kim - CS 325

def changeDP(v, A):
    numCoins = [0 if idx == 0 else float("inf") for idx in range(A + 1)]            #create array that holds number of coins for solution
    lastCoinAdded = [-1 for _ in range(A + 1)]                                      #create array that holds the last coin added
    C = [0 for _ in range(len(v))]                                                  #initiate array c (answer array) with 0

    for j in range(len(v)):                                                         #for every different coin value
        for i in range(1, A + 1):                                                   #for every value up to the answer value
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
