
# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/05/2022
# Description: A function that takes a positive integer parameter and returns the number at that position of
# the Fibonacci sequence.

def fib(num):
    p = 1
    q = 1
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        while num > 2:
            x = p + q
            p = q
            q = x
            num = num - 1

        return x

