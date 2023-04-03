# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 11:12:42 2023

@author: Yazen
"""
def anagram(s):
    #cannot be split into two equal lengths
    #if it is not even
    if len(s)%2 != 0:
        return -1
    
    #split into two contiguous substrings of equal lengths
    firstHalf = s[0:len(s)//2]
    secondHalf = s[len(s)//2:len(s)]
    
    #create the alphabet
    alphabet = [chr(num) for num in [num for num in range(ord('a'), ord('z')+1)]]
    #create an alphabet dictionary
    alphabetDict = dict.fromkeys(alphabet, 0)
    
    #loop through each half
    for i in range(0, len(firstHalf)):
        #the first half contributes to the tally 
        alphabetDict[firstHalf[i]] += 1
        #the second half lessens the tally
        alphabetDict[secondHalf[i]] -= 1
    
    #Now, we have a dictionary which indicates the letters that
    #are mismatched. Matched letters will have a value of 0.
    
    #Simply loop through the dictionary and tally the total
    #Note that we take the absolute value as the second half
    #creates negative values. 
    numToReplace = 0
    for letter in alphabetDict.keys():
        numToReplace += abs(alphabetDict[letter])
        
    #Return half as we are counting every mismatched letter twice
    return numToReplace//2
