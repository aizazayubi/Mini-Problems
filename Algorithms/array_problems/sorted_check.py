def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# Examples
print(is_sorted([1, 3, 5, 7]))
print(is_sorted([1, 5, 3, 7]))

