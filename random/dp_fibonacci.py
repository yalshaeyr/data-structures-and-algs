# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:03:35 2023

@author: Yazen
"""

import time 

#wrapper to time the fibonacci function
def function_timer(func):
    def wrapper(n):
        start = time.time()
        val = func(n)
        end = time.time()
        print(f'{func.__name__} took {end-start:.5f} seconds')
        return val, end-start
    return wrapper

#typical recursive fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

#storage
fib_mem = {0:1, 1:1}

#recursive fibonacci with dynamic programming
def dp_fibonacci(n):
    try:
        return fib_mem[n]
    except KeyError:
        fib_mem[n] = dp_fibonacci(n-1) + dp_fibonacci(n-2)
        return fib_mem[n]

#comparison when n = 35
#call the wrapper directly instead of using a decorator to avoid
#calling the timer for each recursion
val, fast_time = function_timer(fibonacci)(35)
val, slow_time = function_timer(dp_fibonacci)(35)