# Algorithms/array_problems/missing_number.py

def find_missing_number(arr):
    n = len(arr) + 1  # since one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


# Get array input from user
user_input = input("Enter numbers from 1 to n with one missing (separated by space): ")
arr = [int(x) for x in user_input.split()]

missing = find_missing_number(arr)
print("Missing number is:", missing)
