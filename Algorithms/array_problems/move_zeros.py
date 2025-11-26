# Algorithms/array_problems/move_zeros.py

def move_zeros(arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1

# Get array input from user
user_input = input("Enter numbers separated by space: ")
arr = [int(x) for x in user_input.split()]

move_zeros(arr)
print("Array after moving zeros to the end:", arr)
