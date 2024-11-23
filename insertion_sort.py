"""Insertion sort"""
from typing import List


def insertion_sort(arr: List[int]):
	"""do actual insertion sort"""
	n = len(arr) #the array length
	if n == 1: # if list contains one element it is already sorted
		return

	for i in range(1, n):
		current = arr[i]
		prev = i - 1
		while prev >= 0 and current < arr[prev]:
			arr[prev+1] = arr[prev]
			prev -= 1
		arr[prev+1] = current

if __name__ == "__main__":
	array = [1,3,5,2,4]
	insertion_sort(array)
	print(array)
