"""merge sort algorithm"""
from typing import List


def merge(array: List, left: int, middle: int, right: int):
    """do the merge"""
    arr1 = middle - left + 1
    arr2 = right - middle
    L1 = [0] * arr1
    print("arr1 is : {} and arr2 is : {}".format(L1, arr2))

merge([1,2,3,4,5], 0, 2, 4)