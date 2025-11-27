# Algorithms/array_problems/missing_number.py

def find_missing_number(arr):
    # function that takes an array arr.
    n = len(arr) + 1  # If one number is missing from 1 to n, then total count should be array length + 1.
    expected_sum = n * (n + 1) // 2
    # This is the formula for the sum of numbers from 1 to n.
    # (Example: for n=5 → 1+2+3+4+5 = 15)
    actual_sum = sum(arr)
    # Adds all the numbers that actually exist in the array.
    return expected_sum - actual_sum
    # The difference gives the missing number.

# Get array input from user
user_input = input("Enter numbers from 1 to n with one missing (separated by space): ")
arr = [int(x) for x in user_input.split()]

missing = find_missing_number(arr)
print("Missing number is:", missing)
