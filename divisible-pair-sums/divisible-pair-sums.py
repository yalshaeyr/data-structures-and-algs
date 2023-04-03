# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:26:49 2023

@author: Yazen

divisible-pair-sums.py 

Problem description:
    Given a list of integers, find the number of unique pairs of indices i, j 
    such that a[i] + a[j] are divisible by k and i < j. 
    For example, given a = [1, 2, 3, 4, 5] and k = 3:
        The pairs are [0, 1], [0, 4], [1, 3], and [3, 4]
        a[0] + a[1] = 1 + 2 = 3
        a[0] + a[4] = 1 + 5 = 6
        a[1] + a[3] = 2 + 4 = 6
        a[3] + a[4] = 4 + 5 = 9
"""
import time, random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#wrapper to time the divisible-pair-sums functions
def function_timer(func):
    def wrapper(array, k):
        start = time.time()
        val = func(array, k)
        end = time.time()
        print(f'{func.__name__} took {end-start:.5f} seconds')
        return val, end-start
    return wrapper

#Compares quick variant to slow variant
#Slow variant is a brute-force method that will always produce
#the correct result. This is a slow way to confirm the
#accuracy of the quick variant. Might as well grab the results
#while that's happening!
def test_funcs():
    MIN_TESTS = 5 #minimum number of tests
    MAX_TESTS = 20 #max number of tests
    LOW_END = 1 #minimum value for n/k
    HIGH_END = 10**4 #max value for n/k
    #results data frame 
    results = pd.DataFrame({"pass":[], "n":[], "k":[], "slow_time":[], "quick_time":[]})
    #randomise the number of tests
    num_tests = random.randint(MIN_TESTS, MAX_TESTS)
    #inform the user of the number of tests
    print(f"Conducting {num_tests} tests now...")
    #run through the tests
    for test_num in range(num_tests):
        #produce the test list 
        vals = random.sample(range(LOW_END, HIGH_END), random.randint(LOW_END, HIGH_END))
        #produce a random divisor 
        k = random.randint(LOW_END, HIGH_END)
        #inform the user of the current test
        print(f"Test #{test_num+1}... n = {len(vals)} and k = {k}")
        #call the basic function
        slow_count, slow_time = slow_num_divisible(vals, k)
        #call the efficient function
        count, time_taken = num_divisible(vals, k)
        #store the results. Set success to False initially
        curr_results = np.array([False, len(vals), k, slow_time, time_taken])
        #print info messages
        if slow_count != count:
            print(f"Failed test where n = {len(vals)}, k = {k}\n")
        else:
            print("Function passed!")
            curr_results[0] = True #set success to True if passed
        #add the results to the data frame
        results.loc[test_num+1] = curr_results
    return results #return the results

#plot the results retrieved from test_funcs()
def plot_results(results):
    x = results["n"]
    y1 = results["slow_time"]
    y2 = results["quick_time"]
    #two scatter plots 
    plt.plot(x, y1, 'b.', label="Basic")
    plt.plot(x, y2, 'r.', label="Efficient")
    #labelled with a legend
    plt.legend(title="Function")
    #with a title and axes labels
    plt.title("Divisible pair sums")
    plt.xlabel("n")
    plt.ylabel("time (seconds)")
    #display the figure
    plt.show()
                    

#O(n^2) - most basic variant
@function_timer
def slow_num_divisible(array, k):
    count = 0
    #simply test every pair 
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if (array[i] + array[j]) % k == 0:
                count += 1
    return count 

#O(n) - a more efficient variant 
@function_timer
def num_divisible(array, k):
    #basic checks to marginally improve efficiency 
    if k == 1:
        #count every possible pair. This is the same as counting
        #k-1 + k-2 + k-3 + ... + 1
        return sum([i for i in range(1, len(array)-1)])
    #no pairs are possible if the length is one
    if len(array) == 1:
        return 0
    #count is the number of divisible pairs
    #counts is a tally of each element
    count, counts = 0, {}
    #first loop - get modulo k of every element
    for i in range(len(array)):
        array[i] = array[i] % k
        #tally these values
        try:
            counts[array[i]] += 1
        except KeyError:
            counts[array[i]] = 1
    #second loop - count number of pairs
    for elem in array:
        #the complement of the current element modulo k 
        complement = (k-elem)%k
        try:
            #count the number of possible pairs
            #this is simply the number of the element's complements remaining
            count += counts[complement]
            #if the complement is equal to the element, don't consider a 
            #pair with itself
            if complement==elem:
                count -= 1
            #reduce the count to avoid doubling up on pairs
            counts[elem] -= 1
        except KeyError:
            pass 
    return count

#testing and results
results = test_funcs()
plot_results(results)
with open("test_results.txt", "w") as test_results:
    test_results.write(f"{results}")

# For manual test cases
# =============================================================================
# with open('test.txt', 'r') as test_file:
#     try: 
#         n = int(test_file.readline()) 
#         for i in range(n):
#             k = int(test_file.readline())
#             vals = list(map(int, test_file.readline().split()))
#             count, time_taken = num_divisible(vals, k)
#             print(f"For test #{i+1}, the count was {count}")
#     except ValueError: 
#         print("Unable to parse int in test file")
# =============================================================================
