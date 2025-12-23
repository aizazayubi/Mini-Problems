def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None


# Get array input from user
user_input = input("Enter numbers separated by space: ")
arr = [int(x) for x in user_input.split()]

result = second_largest(arr)

if result is None:
    print("No second largest element found.")
else:
    print("Second largest element is:", result)
