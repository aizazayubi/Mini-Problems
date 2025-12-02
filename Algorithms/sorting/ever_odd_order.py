def custom_sort(arr):
    evens = sorted([x for x in arr if x % 2 == 0])
    odds = sorted([x for x in arr if x % 2 != 0], reverse=True)
    return evens + odds

# Example
arr = [7, 2, 9, 4, 3, 8]
print(custom_sort(arr))
