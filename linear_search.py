"""Linear search algorithm"""
from typing import List


def search(arr: List[int], target: int) -> int | None:
    """searches a list and returns index of target"""
    end = len(arr)
    for i in range(end):
        if arr[i] == target:
            return i
    return None

if __name__ == "__main__":
    array = [1,8,9,8,6]
    target = 6
    print(search(array, target))
    