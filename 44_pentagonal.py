import numpy as np
import math

def get_pentagonal(n):
    return int(n*(3*n-1)/2)


def is_pentagonal(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False
    


def analyze_two_pentagonals(j, k):

    P_j = get_pentagonal(j)
    P_k = get_pentagonal(k)

    #print(j, P_j, k, P_k)
    
    sum = P_j + P_k
    diff = P_j - P_k

    if (is_pentagonal(sum) and is_pentagonal(diff)):
        return abs(diff), j, k
    else:
        return None

for j in range(1, 1000000):
    for k in range(1, j):
        result = analyze_two_pentagonals(j, k)
        if result is not None:
            print(result)

