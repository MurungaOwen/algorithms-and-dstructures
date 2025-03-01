#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import accumulate

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sort_desc(arr):
    index = 0
    while index < len(arr):
        for i in range(index+1, len(arr)):
            if arr[i] > arr[index]:
                arr[i], arr[index] = arr[index], arr[i]
        index += 1
    return arr

def miniMaxSum(arr):
    # Write your code here

    max_arr = sort_desc(arr)
    max_sum = list(accumulate(sort_desc(arr)))[3]
    min_sum = list(accumulate(max_arr[::-1]))[3] # just reverse the sorted instead of creating function to sort in asc
    print("{} {}".format(min_sum, max_sum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
