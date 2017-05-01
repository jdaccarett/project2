   #Divide and Conquer - Coin Change Problem
   #Jacqueline Francik - CS 325 

   def changeslow(V, A):

        minCoins = [0 for c in V]
        minCoins[0] = A
        # now we recursively step through the algorithm at every level
        # and find the minimum amount for that level
        for coin in [c for c in V if c <= A]:
            temp = (changeslow(V, A - coin))
            temp[V.index(coin)] += 1
            if sum(minCoins) > sum(temp):
                minCoins = temp
                bestSum = temp
        return (minCoins)
    
        
    finalCoins = changeslow(V, A)
    
    coinSum = sum(finalCoins)
    
    return (finalCoins, coinSum)

