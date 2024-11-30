"""Binary search"""
from typing import List

# requires sorted
def search(arr: List[int], target: int) -> int | None:
    """binary search implementation"""
    start = 0
    end = len(arr) - 1
    while(start <= end):
        mid = (end + start) // 2 # without remainder

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

if __name__ == "__main__":
    arr=[1,4,3,7,4,9]
    print(search(arr, 3))
            