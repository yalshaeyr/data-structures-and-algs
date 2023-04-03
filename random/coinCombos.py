# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:36:01 2023

@author: Yazen
"""


#iterative
def itGetWays(n, c):
    #initialise all to 0
    itWayMem = [0 for i in range(n+1)]
    #set the base case
    itWayMem[0] = 1 
    #store combos
    strCombos = [[] for i in range(0, n+1)]
    strCombos[0] = "0"
    
    #loop through all the coins
    for coin in c:
        #find every combo you can make with this coin
        #from 1->n. We are using a bottom-up approach,
        #so we need all values preceding n to calculate n
        #e.g. Suppose n = 3 and c = [1, 2]
        #the combos using coin = 1 would include 
        #0+1, 1+1, 1+1+1. We stop here because we have reached n.
        #We move on to the next coin to see the combos we can make with it
        #This would be 2, so this includes
        #0+2, 1+2. We stop here because have reached n. Critically, 
        #we skip overlapping combinations. 
        for comboTotal in range(1, len(itWayMem)):
            #The coin must be smaller or equal to the comboTotal, or it
            #will exceed the total we are trying to make.
            if coin <= comboTotal:
                #We have selected the coin, and we need to find the number
                #of ways to get comboTotal. So, we check our list. Note that
                #If we have comboTotal = 3 and coin = 1, we find how many
                #ways we can get 2. There should only be one way so far,
                #which is 1+1. The reason we don't have the other way, 0+2,
                #is because we haven't recorded combos with coin = 2 yet.
                #This helps us avoid overcounting. 
                itWayMem[comboTotal] += itWayMem[comboTotal-coin]
                #visually display the combinations
                for strCombo in strCombos[comboTotal-coin]:
                    currCombo = f"{coin}"
                    if strCombo != "0":
                        currCombo += f"+{strCombo}"
                    strCombos[comboTotal].append(currCombo)
    print(strCombos[n])
    return itWayMem[n]

#recursive