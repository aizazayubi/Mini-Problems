# Algorithms/array_problems/move_zeros.py

def move_zeros(arr):
    non_zero_index = 0  # Track the position for non-zero elements

    # Move non-zero elements forward
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1

# Example usage
arr = [0, 1, 0, 3, 12]
move_zeros(arr)
print(arr)  # Output: [1, 3, 12, 0, 0]
