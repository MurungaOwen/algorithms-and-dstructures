from typing import List

def heapify(array: List, index: int, size: int):
    """
    Create a max heap.
    """
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and array[left] > array[largest]:  # Changed comparison here
        largest = left
    if right < size and array[right] > array[largest]:  # Changed comparison here
        largest = right
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(array, largest, size)

def sort(array: List, size: int):
    print("array before: ", array)
    for i in range(size // 2 - 1, -1, -1):
        heapify(array, i, size)
        print("array as we heapify: ", array)
    print("final heap", array)
    
    for i in range(size - 1, 0, -1):
        array[0], array[i] = array[i], array[0] 
        heapify(array, 0, i)

if __name__ == "__main__":
    array = [1, 3, 5, 7, 2]
    size = len(array)
    print("size is {}".format(size))
    sort(array, size)
    print(array)
