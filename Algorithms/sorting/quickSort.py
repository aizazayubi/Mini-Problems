def quick_sort(arr, low, high):
    if low < high:
        # Partitioning index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Example usage
arr = [5, 2, 9, 1, 5, 6]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 2, 5, 5, 6, 9]
