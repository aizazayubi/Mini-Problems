"""
Problem: Sort an Array of Integers
Given an array of integers, sort the array in ascending order without using built-in sort functions.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]
    print("Original array:", arr)
    print("Bubble Sort:", bubble_sort(arr.copy()))
    print("Quick Sort:", quick_sort(arr.copy()))
