def second_largest(arr):
    if len(arr) < 2:
        return None

    largest = second = float('-inf')

    for x in arr:
        if x > largest:
            second = largest
            largest = x
        elif x != largest and x > second:
            second = x

    return second


# Example
arr = [10, 5, 20, 8]
print(second_largest(arr))  # 10

