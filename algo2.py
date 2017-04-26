

def changegreedy(V, A):
    #variables declared
    i = len(V) - 1
    j = 0
    size = len(V)
    C = [None] * size
    coinsCount= 0;

    #Keeps iterating through the coins passed
    while i >= 0:
        #Finds max of times each coin can go into the amount
        if V[i] <= A:
            number = A // V[i]
            A = A - (number * V[i])
            C[i] = number
            #Increments number of coins
            coinsCount = number + coinsCount

        elif V[i] >= A:
            number = 0
            C[i] = number
        j = j + 1
        i = i -1

    #returns array of coins used & amount of coins used.
    return C, coinsCount




