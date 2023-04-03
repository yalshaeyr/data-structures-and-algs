# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 18:54:10 2023

@author: Yazen
"""

#get input 
vals = list(map(int, input().split()))

#use if you want output sorted
#vals.sort()

def permutations(vals):
    perms = []
    if len(vals)==2:
        return [[vals[0],vals[1]],
                [vals[1],vals[0]]]
    for i in range(0, len(vals)):
        newVals = vals[0:i] + vals[i+1:len(vals)]
        newPerms = permutations(newVals)
        for newPerm in newPerms:
            #no duplicates
            if [vals[i]]+newPerm not in perms:
                perms.append([vals[i]]+newPerm)
    return perms 

perms = permutations(vals)
print(perms)